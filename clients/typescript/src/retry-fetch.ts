export type RetryFetchOptions = {
  maxAttempts?: number;
  baseDelayMs?: number;
  maxDelayMs?: number;
};

const RETRYABLE_STATUS_CODES = new Set([
  408,
  425,
  429,
  500,
  502,
  503,
  504,
]);

export async function retryFetch(
  input: RequestInfo | URL,
  init?: RequestInit,
): Promise<Response> {
  const maxAttempts = 3;
  const baseDelayMs = 250;
  const maxDelayMs = 5_000;

  for (let attempt = 0; attempt < maxAttempts; attempt += 1) {
    try {
      const response = await fetch(input, init);

      const shouldRetry =
        RETRYABLE_STATUS_CODES.has(response.status) &&
        attempt < maxAttempts - 1;

      if (!shouldRetry) {
        return response;
      }

      const retryAfterMs = getRetryAfterMs(response);
      const exponentialDelay = Math.min(
        maxDelayMs,
        baseDelayMs * 2 ** attempt,
      );

      await delay(retryAfterMs ?? exponentialDelay);
    } catch (error) {
      if (attempt >= maxAttempts - 1) {
        throw error;
      }

      const exponentialDelay = Math.min(
        maxDelayMs,
        baseDelayMs * 2 ** attempt,
      );

      await delay(exponentialDelay);
    }
  }

  throw new Error("Retry loop terminated unexpectedly");
}

function getRetryAfterMs(response: Response): number | undefined {
  const value = response.headers.get("retry-after");

  if (value === null) {
    return undefined;
  }

  const seconds = Number(value);

  if (Number.isFinite(seconds)) {
    return Math.max(0, seconds * 1_000);
  }

  const date = Date.parse(value);

  if (Number.isNaN(date)) {
    return undefined;
  }

  return Math.max(0, date - Date.now());
}

function delay(milliseconds: number): Promise<void> {
  return new Promise((resolve) => {
    setTimeout(resolve, milliseconds);
  });
}