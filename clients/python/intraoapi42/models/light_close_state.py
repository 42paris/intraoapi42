from typing import Literal

LightCloseState = Literal["close", "unclose"]

LIGHT_CLOSE_STATE_VALUES: set[LightCloseState] = {
    "close",
    "unclose",
}


def check_light_close_state(value: str) -> LightCloseState:
    if value in LIGHT_CLOSE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIGHT_CLOSE_STATE_VALUES!r}")
