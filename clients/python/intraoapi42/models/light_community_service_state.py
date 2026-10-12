from typing import Literal

LightCommunityServiceState = Literal["beginning", "invalidated", "schedule", "validated"]

LIGHT_COMMUNITY_SERVICE_STATE_VALUES: set[LightCommunityServiceState] = {
    "beginning",
    "invalidated",
    "schedule",
    "validated",
}


def check_light_community_service_state(value: str) -> LightCommunityServiceState:
    if value in LIGHT_COMMUNITY_SERVICE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIGHT_COMMUNITY_SERVICE_STATE_VALUES!r}")
