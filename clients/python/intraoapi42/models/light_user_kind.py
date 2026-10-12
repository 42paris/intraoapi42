from typing import Literal

LightUserKind = Literal["admin", "external", "student"]

LIGHT_USER_KIND_VALUES: set[LightUserKind] = {
    "admin",
    "external",
    "student",
}


def check_light_user_kind(value: str) -> LightUserKind:
    if value in LIGHT_USER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIGHT_USER_KIND_VALUES!r}")
