from typing import Literal

UserCandidatureGender = Literal["female", "male", "other"]

USER_CANDIDATURE_GENDER_VALUES: set[UserCandidatureGender] = {
    "female",
    "male",
    "other",
}


def check_user_candidature_gender(value: str) -> UserCandidatureGender:
    if value in USER_CANDIDATURE_GENDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_CANDIDATURE_GENDER_VALUES!r}")
