from typing import Literal

LightCloseKind = Literal[
    "agu", "black_hole", "deserter", "non_admitted", "other", "pace_unknown", "serious_misconduct", "social_security"
]

LIGHT_CLOSE_KIND_VALUES: set[LightCloseKind] = {
    "agu",
    "black_hole",
    "deserter",
    "non_admitted",
    "other",
    "pace_unknown",
    "serious_misconduct",
    "social_security",
}


def check_light_close_kind(value: str) -> LightCloseKind:
    if value in LIGHT_CLOSE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIGHT_CLOSE_KIND_VALUES!r}")
