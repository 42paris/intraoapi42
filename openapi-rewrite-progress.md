# OpenAPI Rewrite Progress — Intra 42 API

Tracking progress of rewriting the legacy Intra 42 API documentation into a proper OpenAPI 3.1 spec.

## Legend

| Status | Meaning |
|---|---|
| ✅ Done | Schema + operation fully written, tested against a real response |
| 🚧 In progress | Created but not fully tested / needs review |
| ❌ Impossible | Endpoint doesn't return anything, is deprecated, or can't be verified |
| ⏳ To do | Not started yet |
| ⚠️ Blocked | Waiting on missing info (enum values, unclear fields, access rights) |

---

## Accreditations

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/accreditations` | 🚧 In progress | |
| GET | `/accreditations/{id}` | 🚧 In progress | |
| POST | `/accreditations` | ⏳ To do | |
| PATCH | `/accreditations/{id}` | ⏳ To do | |
| PUT | `/accreditations/{id}` | ⏳ To do | |
| DELETE | `/accreditations/{id}` | ⏳ To do | |

## Achievements

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/achievements` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/achievements` | ⏳ To do | |
| GET | `/campus/{campus_id}/achievements` | ⏳ To do | |
| GET | `/titles/{title_id}/achievements` | ⏳ To do | |
| GET | `/achievements/{id}` | ⏳ To do | |
| POST | `/achievements` | ⏳ To do | |
| PATCH | `/achievements/{id}` | ⏳ To do | |
| PUT | `/achievements/{id}` | ⏳ To do | |
| DELETE | `/achievements/{id}` | ⏳ To do | |

## Achievements users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/achievements/{achievement_id}/achievements_users` | ⏳ To do | |
| GET | `/achievements_users` | ⏳ To do | |
| GET | `/achievements_users/{id}` | ⏳ To do | |
| POST | `/achievements_users` | ⏳ To do | |
| PATCH | `/achievements_users/{id}` | ⏳ To do | |
| PUT | `/achievements_users/{id}` | ⏳ To do | |
| DELETE | `/achievements_users/{id}` | ⏳ To do | |

## Alumnized users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/alumnized_users` | ⏳ To do | |

## Amendments

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/amendments` | ⏳ To do | |
| GET | `/users/{user_id}/amendments` | ⏳ To do | |
| GET | `/internships/{internship_id}/amendments` | ⏳ To do | |
| GET | `/amendments/{id}` | ⏳ To do | |
| POST | `/amendments` | ⏳ To do | |
| DELETE  | `/amendments/{id}` | ⏳ To do | |

## Announcements

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/announcements/{id}` | ⏳ To do | |
| POST | `/announcements` | ⏳ To do | |
| POST | `/cursus/{cursus_id}/announcements` | ⏳ To do | |
| PATCH | `/announcements/{id}` | ⏳ To do | |
| PUT | `/announcements/{id}` | ⏳ To do | |
| DELETE | `/announcements/{id}` | ⏳ To do | |

## Anti grav units

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/anti_grav_units` | ⏳ To do | |
| GET | `/anti_grav_units/{id}` | ⏳ To do | |

## Anti grav units users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/anti_grav_units_users` | ⏳ To do | |
| GET | `/users/{user_id}/anti_grav_units_users` | ⏳ To do | |
| GET | `/campus/{campus_id}/anti_grav_units_users` | ⏳ To do | |
| GET | `/anti_grav_units_users/{id}` | ⏳ To do | |
| POST | `/anti_grav_units_users` | ⏳ To do | |
| PATCH | `/anti_grav_units_users/{id}` | ⏳ To do | |
| PUT | `/anti_grav_units_users{id}` | ⏳ To do | |

## Apps

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/apps` | ⏳ To do | |
| GET | `/users/{user_id}/apps` | ⏳ To do | |
| GET | `/apps/{id}` | ⏳ To do | |

## Attachments

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions/{project_session_id}/attachments` | ⏳ To do | |
| GET | `/projects/{project_id}/attachments` | ⏳ To do | |
| GET | `/attachments` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/attachments/{id}` | ⏳ To do | |
| GET | `/attachments/{id}` | ⏳ To do | |
| POST | `/projects/{project_id}/attachments` | ⏳ To do | |
| PATCH | `/attachments/{id}` | ⏳ To do | |
| PUT | `/attachments/{id}` | ⏳ To do | |
| DELETE | `/attachments/{id}` | ⏳ To do | |

## Balances

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/balances` | ⏳ To do | |
| GET | `/pools/{pools_id}/balances` | ⏳ To do | |
| GET | `/balances/{id}` | ⏳ To do | |
| GET | `/pools/{pools_id}/balances/{id}` | ⏳ To do | |
| PATCH | `/balances/{id}` | ⏳ To do | |
| PUT | `/balances/{id}` | ⏳ To do | |
| PATCH | `/pools/{pools_id}/balances/{id}` | ⏳ To do | |
| PUT | `/pools/{pools_id}/balances/{id}` | ⏳ To do | |

## Bloc deadlines

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/bloc_deadlines` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/bloc_deadlines` | ⏳ To do | |
| GET | `/bloc_deadlines/{id}` | ⏳ To do | |
| POST | `/bloc_deadlines` | ⏳ To do | |
| PATCH | `/bloc_deadlines/{id}` | ⏳ To do | |
| PUT | `/bloc_deadlines/{id}` | ⏳ To do | |

## Blocs

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/blocs` | ⏳ To do | |
| GET | `/blocs/{id}` | ⏳ To do | |

## Broadcasts

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/campus/{campus_id}/broadcasts` | ⏳ To do | |

## Campus

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/campus` | ⏳ To do | |
| GET | `/campus/{id}` | ⏳ To do | |
| POST | `/campus` | ⏳ To do | |
| PATCH | `/campus/{id}` | ⏳ To do | |
| PUT | `/campus/{id}` | ⏳ To do | |
| GET | `/campus/{campus_id}/stats` | ⏳ To do | |

## Campus users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/campus_users` | ⏳ To do | |
| GET | `/users/{user_id}/campus_users` | ⏳ To do | |
| GET | `/campus_users/{id}` | ⏳ To do | |
| POST | `/campus_users` | ⏳ To do | |
| POST | `/users/{user_id}/campus_users` | ⏳ To do | |
| POST | `/campus_users/{id}/set_as_primary` | ⏳ To do | |

## Certificates

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/certificates` | ⏳ To do | |
| GET | `/certificates/{id}` | ⏳ To do | |

## Certificates users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/certificates_users` | ⏳ To do | |
| GET | `/certificates/{certificate_id}/certificates_users` | ⏳ To do | |
| GET | `/users/{user_id}/certificates_users` | ⏳ To do | |
| GET | `/certificates_users/{id}` | ⏳ To do | |
| DELETE | `/certificates_users/{id}` | ⏳ To do | |

## Closes

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/closes` | 🚧 In progress | |
| GET | `/closes/{id}` | 🚧 In progress | |
| GET | `/users/{user_id}/closes` | 🚧 In progress | |
| POST | `/closes` | ⏳ To do | |
| POST | `/users/{user_id}/closes` | ⏳ To do | |
| PATCH | `/closes/{id}` | ⏳ To do | |
| PUT | `/closes/{id}` | ⏳ To do | |
| DELETE | `/closes/{id}` | ⏳ To do | |
| PATCH | `/closes/{id}/unclose` | ⏳ To do | |
| PUT | `/closes/{id}/unclose` | ⏳ To do | |
| PATCH | `/closes/{id}/close` | ⏳ To do | |
| PUT | `/closes/{id}/close` | ⏳ To do | |

## Clusters

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/clusters` | ⏳ To do | |
| GET | `/clusters/{id}` | ⏳ To do | |

## Coalitions

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/coalitions` | ⏳ To do | |
| GET | `/users/{user_id}/coalitions` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/coalitions` | ⏳ To do | |
| GET | `/coalitions/{id}` | ⏳ To do | |
| POST | `/coalitions` | ⏳ To do | |
| PATCH | `/coalitions/{id}` | ⏳ To do | |
| PUT | `/coalitions/{id}` | ⏳ To do | |

## Coalitions users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/coalitions/{coalition_id}/coalitions_users` | ⏳ To do | |
| GET | `/coalitions_users` | ⏳ To do | |
| GET | `/users/{user_id}/coalitions_users` | ⏳ To do | |
| GET | `/coalitions_users/{id}` | ⏳ To do | |
| POST | `/coalitions_users` | ⏳ To do | |
| PATCH | `/coalitions_users/{id}` | ⏳ To do | |
| PUT | `/coalitions_users/{id}` | ⏳ To do | |
| DELETE | `/coalitions_users/{id}` | ⏳ To do | |

## Commands

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/products/{product_id}/commands` | ⏳ To do | |
| GET | `/campus/{campus_id}/products/{product_id}/commands` | ⏳ To do | |

## Community services

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/closes/{close_id}/community_services` | ⏳ To do | |
| GET | `/community_services` | ⏳ To do | |
| GET | `/community_services/{id}` | ⏳ To do | |
| PUT | `/community_services/{id}/validate` | ⏳ To do | |
| PATCH | `/community_services/{id}/validate` | ⏳ To do | |
| PUT | `/community_services/{id}/invalidate` | ⏳ To do | |
| PATCH | `/community_services/{id}/invalidate` | ⏳ To do | |
| POST | `/community_services` | ⏳ To do | |
| PATCH | `/community_services/{id}` | ⏳ To do | |
| PUT | `/community_services/{id}` | ⏳ To do | |
| DELETE | `/community_services/{id}` | ⏳ To do | |

## Companies

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/companies` | ⏳ To do | |
| GET | `/companies/{id}` | ⏳ To do | |
| GET | `/companies/{company_id}/subscribed_users` | ⏳ To do | |
| GET | `/companies/{company_id}/internships_users` | ⏳ To do | |

## Correction point historics

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/users/{user_id}/correction_point_historics` | ⏳ To do | |

## Cursus

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/cursus` | ⏳ To do | |
| GET | `/cursus/{id}` | ⏳ To do | |
| POST | `/cursus` | ⏳ To do | |
| PATCH | `/cursus/{id}` | ⏳ To do | |
| PUT | `/cursus/{id}` | ⏳ To do | |
| DELETE | `/cursus/{id}` | ⏳ To do | |

## Cursus users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/cursus_users` | ⏳ To do | |
| GET | `/users/{user_id}/cursus_users` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/cursus_users` | ⏳ To do | |
| GET | `/cursus_users/{id}` | ⏳ To do | |
| POST | `/cursus_users` | ⏳ To do | |
| POST | `/users/{user_id}/cursus_users` | ⏳ To do | |
| PATCH | `/cursus_users/{id}` | ⏳ To do | |
| PUT | `/cursus_users/{id}` | ⏳ To do | |
| DELETE | `/cursus_users/{id}` | ⏳ To do | |

## Dashes

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/dashes` | ⏳ To do | |
| GET | `/dashes/{id}` | ⏳ To do | |
| POST | `/dashes` | ⏳ To do | |
| PATCH | `/dashes/{id}` | ⏳ To do | |
| PUT | `/dashes/{id}` | ⏳ To do | |
| DELETE | `/dashes/{id}` | ⏳ To do | |

## Dashes users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/dashes_users` | ⏳ To do | |
| GET | `/dashes/{dash_id}/dashes_users` | ⏳ To do | |
| GET | `/dashes_users/{id}` | ⏳ To do | |
| POST | `/dashes_users` | ⏳ To do | |
| PATCH | `/dashes_users/{id}` | ⏳ To do | |
| PUT | `/dashes_users/{id}` | ⏳ To do | |
| DELETE | `/dashes_users/{id}` | ⏳ To do | |

## Endpoints

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/endpoints` | ⏳ To do | |
| GET | `/endpoints/{id}` | ⏳ To do | |
| POST | `/endpoints` | ⏳ To do | |
| PATCH | `/endpoints/{id}` | ⏳ To do | |
| PUT | `/endpoints/{id}` | ⏳ To do | |
| DELETE | `/endpoints/{id}` | ⏳ To do | |
| POST | `/endpoints/{id}/callback` | ⏳ To do | |

## Evaluations

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/evaluations` | ⏳ To do | |
| GET | `/evaluations/{id}` | ⏳ To do | |
| POST | `/evaluations` | ⏳ To do | |
| PATCH | `/evaluations/{id}` | ⏳ To do | |
| PUT | `/evaluations/{id}` | ⏳ To do | |
| DELETE | `/evaluations/{id}` | ⏳ To do | |

## Events

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/cursus/{cursus_id}/events` | ⏳ To do | |
| GET | `/campus/{campus_id}/events` | ⏳ To do | |
| GET | `/campus/{campus_id}/cursus/{cursus_id}/events` | ⏳ To do | |
| GET | `/users/{user_id}/events` | ⏳ To do | |
| GET | `/events` | ⏳ To do | |
| GET | `/events/{id}` | ⏳ To do | |
| POST | `/events` | ⏳ To do | |
| PATCH | `/events/{id}` | ⏳ To do | |
| PUT | `/events/{id}` | ⏳ To do | |
| DELETE | `/events/{id}` | ⏳ To do | |

## Events users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/users/{user_id}/events_users` | ⏳ To do | |
| GET | `/events/{envent_id}/events_users` | ⏳ To do | |
| GET | `/events_users` | ⏳ To do | |
| GET | `/events_users/{id}` | ⏳ To do | |
| POST | `/events_users` | ⏳ To do | |
| PATCH | `/events_users/{id}` | ⏳ To do | |
| PUT | `/events_users/{id}` | ⏳ To do | |
| DELETE | `/events_users/{id}` | ⏳ To do | |

## Exams

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/cursus/{cursus_id}/exams` | ⏳ To do | |
| GET | `/campus/{campus_id}/exams` | ⏳ To do | |
| GET | `/campus/{campus_id}/cursus/{cursus_id}/exams` | ⏳ To do | |
| GET | `/users/{user_id}/exams` | ⏳ To do | |
| GET | `/projects/{project_id}/exams` | ⏳ To do | |
| GET | `/exams` | ⏳ To do | |
| GET | `/exams/{id}` | ⏳ To do | |
| POST | `/exams` | ⏳ To do | |
| PATCH | `/exams/{id}` | ⏳ To do | |
| PUT | `/exams/{id}` | ⏳ To do | |
| DELETE | `/exams/{id}` | ⏳ To do | |

## Exams users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/exams/{exam_id}/exams_users` | ⏳ To do | |
| POST | `/exams/{exam_id}/exams_users` | ⏳ To do | |
| DELETE | `/exams/{exam_id}/exams_users/{id}` | ⏳ To do | |

## Experiences

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/experiences` | ⏳ To do | |
| GET | `/campus/{campus_id}/experiences` | ⏳ To do | |
| GET | `/projects_users/{projects_user_id}/experiences` | ⏳ To do | |
| GET | `/users/{user_id}/experiences` | ⏳ To do | |
| GET | `/skills/{skill_id}/experiences` | ⏳ To do | |
| GET | `/partnerships_users/{partnerships_user_id}/experiences` | ⏳ To do | |
| GET | `/experiences/{id}` | ⏳ To do | |
| POST | `/experiences` | ⏳ To do | |
| PATCH | `/experiences/{id}` | ⏳ To do | |
| PUT | `/experiences/{id}` | ⏳ To do | |
| DELETE | `/experiences/{id}` | ⏳ To do | |

## Expertises

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/expertises` | ⏳ To do | |
| GET | `/expertises/{id}` | ⏳ To do | |
| POST | `/expertises` | ⏳ To do | |
| PATCH | `/expertises/{id}` | ⏳ To do | |
| PUT | `/expertises/{id}` | ⏳ To do | |
| DELETE | `/expertises/{id}` | ⏳ To do | |
| GET | `/expertises` | ⏳ To do | |
| GET | `/expertises/{id}` | ⏳ To do | |
| POST | `/expertises` | ⏳ To do | |
| PATCH | `/expertises/{id}` | ⏳ To do | |
| PUT | `/expertises/{id}` | ⏳ To do | |
| DELETE | `/expertises/{id}` | ⏳ To do | |

## Expertises users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/expertises/{expertise_id}/expertises_users` | ⏳ To do | |
| GET | `/users/{user_id}/expertises_users` | ⏳ To do | |
| GET | `/expertises_users` | ⏳ To do | |
| GET | `/expertises_users/{id}` | ⏳ To do | |
| POST | `/expertises/{expertise_id}/expertises_users` | ⏳ To do | |
| POST | `/users/{user_id}/expertises_users` | ⏳ To do | |
| POST | `/expertises_users` | ⏳ To do | |
| PATCH | `/expertises_users/{id}` | ⏳ To do | |
| PUT | `/expertises_users/{id}` | ⏳ To do | |
| DELETE | `/expertises_users/{id}` | ⏳ To do | |
| PATCH | `/expertises_users/{id}` | ⏳ To do | |

## Feedbacks

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/events/{event_id}/feedbacks` | ⏳ To do | |
| GET | `/feedbacks` | ⏳ To do | |
| GET | `/scale_teams/{scale_team_id}/feedbacks` | ⏳ To do | |
| GET | `/events/{event_id}/feedbacks/{id}` | ⏳ To do | |
| GET | `/feedbacks/{id}` | ⏳ To do | |
| GET | `/scale_teams/{scale_team_id}/feedbacks/{id}` | ⏳ To do | |
| POST | `/events/{event_id}/feedbacks` | ⏳ To do | |
| POST | `/feedbacks` | ⏳ To do | |
| POST | `/scale_teams/{scale_team_id}/feedbacks` | ⏳ To do | |
| PATCH | `/events/{event_id}/feedbacks/{id}` | ⏳ To do | |
| PUT | `/events/{event_id}/feedbacks/{id}` | ⏳ To do | |
| PATCH | `/feedbacks/{id}` | ⏳ To do | |
| PUT | `/feedbacks/{id}` | ⏳ To do | |
| PATCH | `/scale_teams/{scale_team_id}/feedbacks/{id}` | ⏳ To do | |
| PUT | `/scale_teams/{scale_team_id}/feedbacks/{id}` | ⏳ To do | |
| DELETE | `/events/{event_id}/feedbacks/{id}` | ⏳ To do | |
| DELETE | `/feedbacks/{id}` | ⏳ To do | |
| DELETE | `/scale_teams/{scale_team_id}/feedbacks/{id}` | ⏳ To do | |


## Flags

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/v2/flags` | ⏳ To do | |

## Flash users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/flashes/{flash_id}/flash_users` | ⏳ To do | |
| GET | `/flash_users` | ⏳ To do | |
| GET | `/flashes/{flash_id}/flash_users/{id}` | ⏳ To do | |
| GET | `/flash_users/{id}` | ⏳ To do | |
| POST | `/flashes/{flash_id}/flash_users` | ⏳ To do | |
| POST | `/flash_users` | ⏳ To do | |

## Flashes

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/flashes` | ⏳ To do | |
| GET | `/flashes/{id}` | ⏳ To do | |
| POST | `/flashes` | ⏳ To do | |

## Gitlab users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/users/{user_id}/gitlab_users` | ⏳ To do | |

## Groups

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/groups` | ⏳ To do | |
| GET | `/users/{user_id}/groups` | ⏳ To do | |
| GET | `/groups/{id}` | ⏳ To do | |

## Groups users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/groups_users` | ⏳ To do | |
| GET | `/groups/{group_id}/groups_users` | ⏳ To do | |
| GET | `/users/{user_id}/groups_users` | ⏳ To do | |
| GET | `/groups_users/{id}` | ⏳ To do | |
| POST | `/groups_users` | ⏳ To do | |
| PATCH | `/groups_users/{id}` | ⏳ To do | |
| PUT | `/groups_users/{id}` | ⏳ To do | |
| DELETE | `/groups_users/{id}` | ⏳ To do | |

## Internships

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/internships` | 🚧 In progress | |
| GET | `/internships/{id}` | 🚧 In progress | |
| GET | `/users/{user_id}/internships` | 🚧 In progress | |
| GET | `/users/{user_id}/internships/{id}` | 🚧 In progress | |
| POST | `/internships` | ⏳ To do | |
| PATCH | `/internships/{id}` | ⏳ To do | |
| PUT | `/internships/{id}` | ⏳ To do | |
| PATCH | `/users/{user_id}/internships/{id}` | ⏳ To do | |
| PUT | `/users/{user_id}/internships/{id}` | ⏳ To do | |
| DELETE | `/internships/{id}` | ⏳ To do | |

## Journals

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/campus/{campus_id}/journals` | ⏳ To do | |

## Languages

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/languages` | ⏳ To do | |
| GET | `/languages/{id}` | 🚧 In progress | |
| POST | `/languages` | ⏳ To do | |
| PATCH | `/languages/{id}` | ⏳ To do | |
| PUT | `/languages/{id}` | ⏳ To do | |
| DELETE | `/languages/{id}` | ⏳ To do | |

## Languages users

| Method | Path | Status | Notes |
|---|---|---|---|
| POST | `/users/{user_id}/languages_users` | ⏳ To do | |
| POST | `/languages_users` | ⏳ To do | |
| PATCH | `/users/{user_id}/languages_users/{id}` | ⏳ To do | |
| PUT | `/users/{user_id}/languages_users/{id}` | ⏳ To do | |
| PATCH | `/languages_users/{id}` | ⏳ To do | |
| PUT | `/languages_users/{id}` | ⏳ To do | |
| DELETE | `/users/{user_id}/languages_users/{id}` | ⏳ To do | |
| DELETE | `/languages_users/{id}` | ⏳ To do | |

## Levels

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/levels` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/levels` | ⏳ To do | |

## Locations

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/locations` | ⏳ To do | |
| GET | `/users/{user_id}/locations` | ⏳ To do | |
| GET | `/campus/{campus_id}/locations` | ⏳ To do | |
| GET | `/locations/{id}` | ⏳ To do | |
| POST | `/locations` | ⏳ To do | |
| POST | `/users/{user_id}/locations` | ⏳ To do | |
| PATCH | `/locations/{id}` | ⏳ To do | |
| PUT | `/locations/{id}` | ⏳ To do | |
| PATCH | `/users/{user_id}/locations/{id}` | ⏳ To do | |
| PUT | `/users/{user_id}/locations/{id}` | ⏳ To do | |
| DELETE | `/locations/{id}` | ⏳ To do | |
| DELETE | `/campus/{campus_id}/locations/end_all` | ⏳ To do | |

## Mailings

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/mailings` | ⏳ To do | |
| GET | `/users/{user_id}/mailings` | ⏳ To do | |
| GET | `/mailings/{id}` | ⏳ To do | |
| POST | `/mailings` | ⏳ To do | |
| PATCH | `/mailings/{id}` | ⏳ To do | |
| PUT | `/mailings/{id}` | ⏳ To do | |
| DELETE | `/mailings/{id}` | ⏳ To do | |

## Notes

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/users/{user_id}/notes` | ⏳ To do | |
| GET | `/campus/{campus_id}/notes` | ⏳ To do | |
| GET | `/notes` | ⏳ To do | |
| GET | `/notes/{id}` | ⏳ To do | |
| POST | `/notes` | ⏳ To do | |
| PATCH | `/notes/{id}` | ⏳ To do | |
| PUT | `/notes/{id}` | ⏳ To do | |
| DELETE | `/notes/{id}` | ⏳ To do | |

## Notions

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/cursus/{cursus_id}/notions` | ⏳ To do | |
| GET | `/tags/{tag_id}/notions` | ⏳ To do | |
| GET | `/notions` | ⏳ To do | |
| GET | `/notions/{id}` | ⏳ To do | |
| POST | `/notions` | ⏳ To do | |
| PATCH | `/notions/{id}` | ⏳ To do | |
| PUT | `/notions/{id}` | ⏳ To do | |
| DELETE | `/notions/{id}` | ⏳ To do | |

## Offers

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/offers` | ⏳ To do | |
| GET | `/offers/{id}` | ⏳ To do | |
| POST | `/offers` | ⏳ To do | |

## Offers users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/offers/{offer_id}/offers_users` | ⏳ To do | |
| GET | `/users/{user_id}/offers_users` | ⏳ To do | |
| GET | `/offers_users` | ⏳ To do | |
| GET | `/offers_users/{id}` | ⏳ To do | |

## Params project sessions rules

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions_rules/{project_sessions_rule_id}/params_project_sessions_rules` | ⏳ To do | |
| GET | `/params_project_sessions_rules` | ⏳ To do | |
| GET | `/params_project_sessions_rules/{id}` | ⏳ To do | |
| POST | `/project_sessions_rules/{project_sessions_rule_id}/params_project_sessions_rules` | ⏳ To do | |
| POST | `/params_project_sessions_rules` | ⏳ To do | |
| PATCH | `/params_project_sessions_rules/{id}` | ⏳ To do | |
| PUT | `/params_project_sessions_rules/{id}` | ⏳ To do | |

## Partnerships

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/partnerships` | ⏳ To do | |
| GET | `/partnerships/{id}` | ⏳ To do | |
| POST | `/partnerships` | ⏳ To do | |
| PATCH | `/partnerships/{id}` | ⏳ To do | |
| PUT | `/partnerships/{id}` | ⏳ To do | |
| DELETE | `/partnerships/{id}` | ⏳ To do | |

## Partnerships users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/partnerships/{partnerships_id}/partnerships_users` | ⏳ To do | |
| GET | `/partnerships_users` | ⏳ To do | |
| GET | `/partnerships_users/{id}` | ⏳ To do | |
| POST | `/partnerships/{partnership_id}/partnerships_users` | ⏳ To do | |
| POST | `/partnerships_users` | ⏳ To do | |
| PATCH | `/partnerships_users/{id}` | ⏳ To do | |
| PUT | `/partnerships_users/{id}` | ⏳ To do | |
| DELETE | `/partnerships_users/{id}` | ⏳ To do | |

## Patronages

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/patronages` | ⏳ To do | |
| GET | `/users/{user_id}/patronages` | ⏳ To do | |
| GET | `/patronages/{id}` | ⏳ To do | |
| POST | `/patronages` | ⏳ To do | |
| POST | `/users/{user_id}/patronages` | ⏳ To do | |
| PATCH | `/patronages/{id}` | ⏳ To do | |
| PUT | `/patronages/{id}` | ⏳ To do | |
| DELETE | `/patronages/{id}` | ⏳ To do | |

## Patronages reports

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/patronages_reports` | ⏳ To do | |
| GET | `/users/{user_id}/patronages_reports` | ⏳ To do | |
| GET | `/patronages/{patronage_id}/patronages_reports` | ⏳ To do | |
| GET | `/reports/{report_id}/patronages_reports` | ⏳ To do | |
| GET | `/patronages_reports/{id}` | ⏳ To do | |
| POST | `/patronages_reports` | ⏳ To do | |
| POST | `/users/{user_id}/patronages_reports` | ⏳ To do | |
| POST | `/patronages/{patronage_id}/patronages_reports` | ⏳ To do | |
| POST | `/reports/{report_id}/patronages_reports` | ⏳ To do | |
| PATCH | `/patronages_reports/{id}` | ⏳ To do | |
| PUT | `/patronages_reports/{id}` | ⏳ To do | |
| DELETE | `/patronages_reports/{id}` | ⏳ To do | |

## Pools

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/pools` | ⏳ To do | |
| GET | `/pools/{id}` | ⏳ To do | |
| POST | `/pools/{id}/points/add` | ⏳ To do | |
| DELETE | `/pools/{id}/points/remove` | ⏳ To do | |

## Products

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/products` | ⏳ To do | |
| GET | `/campus/{campus_id}/products` | ⏳ To do | |
| GET | `/products/{id}` | ⏳ To do | |
| GET | `/campus/{campus_id}/products/{id}` | ⏳ To do | |
| POST | `/products` | ⏳ To do | |
| POST | `/campus/{campus_id}/products` | ⏳ To do | |
| PATCH | `/products/{id}` | ⏳ To do | |
| PUT | `/products/{id}` | ⏳ To do | |
| PATCH | `/campus/{campus_id}/products/{id}` | ⏳ To do | |
| PUT | `/campus/{campus_id}/products/{id}` | ⏳ To do | |
| DELETE | `/products/{id}` | ⏳ To do | |
| DELETE | `/campus/{campus_id}/products/{id}` | ⏳ To do | |

## Project data

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_data` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/project_data` | ⏳ To do | |
| GET | `/project_data/{id}` | ⏳ To do | |
| POST | `/project_data` | ⏳ To do | |
| PATCH | `/project_data/{id}` | ⏳ To do | |
| PUT | `/project_data/{id}` | ⏳ To do | |
| DELETE | `/project_data/{id}` | ⏳ To do | |

## Project sessions

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions/{project_session_id}/teams` | 🚧 In progress | |
| GET | `/projects/{project_id}/project_sessions` | ⏳ To do | |
| GET | `/project_sessions` | ⏳ To do | |
| GET | `/project_sessions/{id}` | ⏳ To do | |

## Project sessions rules

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions/{project_session_id}/project_sessions_rules` | ⏳ To do | |
| GET | `/project_sessions_rules` | ⏳ To do | |
| GET | `/project_sessions_rules/{id}` | ⏳ To do | |
| POST | `/project_sessions/{project_session_id}/project_sessions_rules` | ⏳ To do | |
| POST | `/project_sessions_rules` | ⏳ To do | |
| PATCH | `/project_sessions_rules/{id}` | ⏳ To do | |
| PUT | `/project_sessions_rules/{id}` | ⏳ To do | |

## Project sessions skills

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions_skills` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/project_sessions_skills` | ⏳ To do | |
| GET | `/skills/{skill_id}/project_sessions_skills` | ⏳ To do | |
| GET | `/project_sessions_skills/{id}` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/project_sessions_skills/{id}` | ⏳ To do | |

## Projects

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/projects/{project_id}/projects_users` | 🚧 In progress | |
| GET | `/projects/{project_id}/teams` | 🚧 In progress | |
| GET | `/cursus/{cursus_id}/projects` | ⏳ To do | |
| GET | `/projects/{project_id}/projects` | ⏳ To do | |
| GET | `/projects` | ⏳ To do | |
| GET | `/me/projects` | ⏳ To do | |
| GET | `/projects/{id}` | ⏳ To do | |
| POST | `/projects` | ⏳ To do | |
| PATCH | `/projects/{id}` | ⏳ To do | |
| PUT | `/projects/{id}` | ⏳ To do | |
| DELETE | `/projects/{id}` | ⏳ To do | |
| PATCH | `/projects/{id}/retry` | ⏳ To do | |
| PUT | `/projects/{id}/retry` | ⏳ To do | |

## Projects users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/projects_users` | 🚧 In progress | |
| GET | `/projects_users/{id}` | 🚧 In progress | |
| POST | `/projects_users` | 🚧 In progress | |
| PATCH | `/projects_users/{id}` | 🚧 In progress | |
| PUT | `/projects_users/{id}` | 🚧 In progress | |
| GET | `/users/{user_id}/projects_users` | 🚧 In progress | |
| GET | `/projects/{project_id}/projects_users` | ⏳ To do | |
| POST | `/projects/{project_id}/projects_users` | ⏳ To do | |
| POST | `/users/{user_id}/projects_users` | ⏳ To do | |
| POST | `/projects/{project_id}/register` | ⏳ To do | |
| DELETE | `/projects_users/{id}` | ⏳ To do | |
| PATCH | `/projects_users/{id}/compile` | ⏳ To do | |
| PUT | `/projects_users/{id}/compile` | ⏳ To do | |
| PATCH | `/projects_users/{id}/retry` | ⏳ To do | |
| PUT | `/projects_users/{id}/retry` | ⏳ To do | |
| POST | `/projects_users/register_childs_and_scales` | ⏳ To do | |
| DELETE | `/projects_users/reset` | ⏳ To do | |
| PATCH | `/projects_users/scale` | ⏳ To do | |

## Quests

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/quests` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/quests` | ⏳ To do | |
| GET | `/campus/{campus_id}/quests` | ⏳ To do | |
| GET | `/users/{user_id}/quests` | ⏳ To do | |
| GET | `/quests/{id}` | ⏳ To do | |
| POST | `/quests` | ⏳ To do | |
| PATCH | `/quests/{id}` | ⏳ To do | |
| PUT | `/quests/{id}` | ⏳ To do | |
| DELETE | `/quests/{id}` | ⏳ To do | |

## Quests users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/quests/{quest_id}/quests_users` | ⏳ To do | |
| GET | `/users/{user_id}/quests_users` | ⏳ To do | |
| GET | `/quests_users` | ⏳ To do | |
| GET | `/quests_users/{id}` | ⏳ To do | |
| POST | `/quests_users` | ⏳ To do | |
| PATCH | `/quests_users/{id}` | ⏳ To do | |
| PUT | `/quests_users/{id}` | ⏳ To do | |
| DELETE | `/quests_users/{id}` | ⏳ To do | |

## Roles

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/roles` | ⏳ To do | |
| GET | `/users/{user_id}/roles` | ⏳ To do | |
| GET | `/roles/{id}` | ⏳ To do | |
| POST | `/roles` | ⏳ To do | |
| PATCH | `/roles/{id}` | ⏳ To do | |
| PUT | `/roles/{id}` | ⏳ To do | |
| DELETE | `/roles/{id}` | ⏳ To do | |

## Roles entities

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/roles/{role_id}/roles_entities` | ⏳ To do | |
| GET | `/roles_entities` | ⏳ To do | |
| GET | `/roles_entities/{id}` | ⏳ To do | |
| POST | `/roles_entities` | ⏳ To do | |
| PATCH | `/roles_entities/{id}` | ⏳ To do | |
| PUT | `/roles_entities/{id}` | ⏳ To do | |
| DELETE | `/roles_entities/{id}` | ⏳ To do | |

## Rules

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/rules` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/rules` | ⏳ To do | |
| GET | `/rules/{id}` | ⏳ To do | |
| POST | `/rules` | ⏳ To do | |
| POST | `/project_sessions/{project_session_id}/rules` | ⏳ To do | |
| PATCH | `/rules/{id}` | ⏳ To do | |
| PUT | `/rules/{id}` | ⏳ To do | |
| DELETE | `/rules/{id}` | ⏳ To do | |

## Scale teams

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions/{project_session_id}/scale_teams` | ⏳ To do | |
| GET | `/scale_teams` | ⏳ To do | |
| GET | `/projects/{project_id}/scale_teams` | ⏳ To do | |
| GET | `/users/{user_id}/scale_teams/as_corrector` | ⏳ To do | |
| GET | `/users/{user_id}/scale_teams/as_corrected` | ⏳ To do | |
| GET | `/users/{user_id}/scale_teams` | ⏳ To do | |
| GET | `/me/scale_teams/as_corrector` | ⏳ To do | |
| GET | `/me/scale_teams/as_corrected` | ⏳ To do | |
| GET | `/me/scale_teams` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/scale_teams/{id}` | ⏳ To do | |
| GET | `/scale_teams/{id}` | ⏳ To do | |
| POST | `/project_sessions/{project_session_id}/scale_teams` | ⏳ To do | |
| POST | `/scale_teams` | ⏳ To do | |
| PATCH | `/project_sessions/{project_session_id}/scale_teams/{id}` | ⏳ To do | |
| PUT | `/project_sessions/{project_session_id}/scale_teams/{id}` | ⏳ To do | |
| PATCH | `/scale_teams/{id}` | ⏳ To do | |
| PUT | `/scale_teams/{id}` | ⏳ To do | |
| DELETE | `/project_sessions/{project_session_id}/scale_teams/{id}` | ⏳ To do | |
| DELETE | `/scale_teams/{id}` | ⏳ To do | |
| POST | `/scale_teams/multiple_create` | ⏳ To do | |

## Scales

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/project_sessions/{project_session_id}/scales` | ⏳ To do | |
| GET | `/scales` | ⏳ To do | |
| GET | `/projects/{project_id}/scales` | ⏳ To do | |
| GET | `/users/{user_id}/scales` | ⏳ To do | |
| GET | `/scales/{id}` | ⏳ To do | |
| POST | `/scales` | ⏳ To do | |
| PATCH | `/scales/{id}` | ⏳ To do | |
| PUT | `/scales/{id}` | ⏳ To do | |
| DELETE | `/scales/{id}` | ⏳ To do | |

## Scores

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/scores` | ⏳ To do | |
| GET | `/coalitions/{coalition_id}/scores` | ⏳ To do | |
| GET | `/coalitions_users/{coalitions_user_id}/scores` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/scores` | ⏳ To do | |
| GET | `/scores/{id}` | ⏳ To do | |
| GET | `/coalitions/{coalition_id}/scores/{id}` | ⏳ To do | |
| GET | `/coalitions_users/{coalitions_user_id}/scores/{id}` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/scores/{id}` | ⏳ To do | |
| POST | `/coalitions/{coalition_id}/scores` | ⏳ To do | |
| DELETE | `/coalitions/{coalition_id}/scores/{id}` | ⏳ To do | |

## Search

| Method | Path | Status | Notes |
|---|---|---|---|
| POST | `/search/users` | ⏳ To do | |
| POST | `/search/projects` | ⏳ To do | |

## Skills

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/skills` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/skills` | ⏳ To do | |
| GET | `/skills/{id}` | ⏳ To do | |
| POST | `/skills` | ⏳ To do | |
| PATCH | `/skills/{id}` | ⏳ To do | |
| PUT | `/skills/{id}` | ⏳ To do | |
| DELETE | `/skills/{id}` | ⏳ To do | |

## Slots

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/slots` | ⏳ To do | |
| GET | `/projects/{project_id}/slots` | ⏳ To do | |
| GET | `/users/{user_id}/slots` | ⏳ To do | |
| GET | `/me/slots` | ⏳ To do | |
| GET | `/slots/{id}` | ⏳ To do | |
| POST | `/slots` | ⏳ To do | |
| PATCH | `/slots/{id}` | ⏳ To do | |
| PUT | `/slots/{id}` | ⏳ To do | |
| DELETE | `/slots/{id}` | ⏳ To do | |

## Squads

| Method | Path | Status | Notes |
|---|---|---|---|
| POST | `/blocs/{bloc_id}/squads` | ⏳ To do | |
| DELETE | `/blocs/{bloc_id}/squads/{id}` | ⏳ To do | |
| DELETE | `/squads/{id}` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/squads` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/squads/{id}` | ⏳ To do | |
| GET | `/squads/{id}` | ⏳ To do | |
| PATCH | `/squads/{id}` | ⏳ To do | |
| PUT | `/squads/{id}` | ⏳ To do | |

## Squads users

| Method | Path | Status | Notes |
|---|---|---|---|
| POST | `/blocs/{bloc_id}/squads_users` | ⏳ To do | |
| DELETE | `/blocs/{bloc_id}/squads_users/{id}` | ⏳ To do | |
| DELETE | `/squads_users/{id}` | ⏳ To do | |
| GET | `/blocs/{bloc_id}/squads_users` | ⏳ To do | |
| PATCH | `/squads_users/{id}` | ⏳ To do | |
| PUT | `/squads_users/{id}` | ⏳ To do | |

## Subnotions

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/notions/{notion_id}/subnotions` | ⏳ To do | |
| GET | `/subnotions` | ⏳ To do | |
| GET | `/subnotions/{id}` | ⏳ To do | |
| POST | `/subnotions` | ⏳ To do | |
| PATCH | `/subnotions/{id}` | ⏳ To do | |
| PUT | `/subnotions/{id}` | ⏳ To do | |
| DELETE | `/subnotions/{id}` | ⏳ To do | |

## Tags

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/projects/{project_id}/tags` | ⏳ To do | |
| GET | `/issues/{issue_id}/tags` | ⏳ To do | |
| GET | `/notions/{notion_id}/tags` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/tags` | ⏳ To do | |
| GET | `/users/{user_id}/tags` | ⏳ To do | |
| GET | `/tags` | ⏳ To do | |
| GET | `/tags/{id}` | ⏳ To do | |
| POST | `/tags` | ⏳ To do | |
| PATCH | `/tags/{id}` | ⏳ To do | |
| PUT | `/tags/{id}` | ⏳ To do | |
| DELETE | `/tags/{id}` | ⏳ To do | |

## Tags users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/tags_users` | ⏳ To do | |
| GET | `/users/{user_id}/tags_users` | ⏳ To do | |
| GET | `/cursus/{cursus_id}/tags_users` | ⏳ To do | |
| GET | `/campus/{campus_id}/tags_users` | ⏳ To do | |
| GET | `/tags/{tag_id}/tags_users` | ⏳ To do | |
| GET | `/tags_users/{id}` | ⏳ To do | |
| POST | `/tags_users` | ⏳ To do | |
| PATCH | `/tags_users/{id}` | ⏳ To do | |
| PUT | `/tags_users/{id}` | ⏳ To do | |
| DELETE | `/tags_users/{id}` | ⏳ To do | |

## Teams

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/teams` | 🚧 In progress | |
| GET | `/me/teams` | 🚧 In progress | |
| GET | `/teams/{id}` | 🚧 In progress | |
| PATCH | `/teams/{id}` | 🚧 In progress | |
| PUT | `/teams/{id}` | 🚧 In progress | |
| POST | `/teams/{id}/reset_team_uploads` | 🚧 In progress | |
| GET | `/users/{user_id}/teams` | 🚧 In progress | |
| GET | `/users/{user_id}/projects/{project_id}/teams` | 🚧 In progress | |
| GET | `/projects/{project_id}/teams` | 🚧 In progress | |
| GET | `/cursus/{cursus_id}/teams` | ⏳ To do | |
| GET | `/project_sessions/{project_session_id}/teams` | ⏳ To do | |
| POST | `/teams` | ⏳ To do | |
| DELETE | `/teams/{id}` | ⏳ To do | |

## Teams uploads

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/teams/{team_id}/teams_uploads` | ⏳ To do | |
| GET | `/teams_uploads` | ⏳ To do | |
| GET | `/teams_uploads/{id}` | ⏳ To do | |
| POST | `/teams_uploads` | ⏳ To do | |
| PATCH | `/teams_uploads/{id}` | ⏳ To do | |
| PUT | `/teams_uploads/{id}` | ⏳ To do | |
| DELETE | `/teams_uploads/{id}` | ⏳ To do | |
| POST | `/teams_uploads/multiple_create` | ⏳ To do | |

## Teams users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/teams_users` | ⏳ To do | |
| GET | `/users/{user_id}/teams_users` | ⏳ To do | |
| GET | `/teams/{team_id}/teams_users` | ⏳ To do | |
| GET | `/teams_users/{id}` | ⏳ To do | |
| POST | `/teams_users` | ⏳ To do | |
| PATCH | `/teams_users/{id}` | ⏳ To do | |
| PUT | `/teams_users/{id}` | ⏳ To do | |
| DELETE | `/teams_users/{id}` | ⏳ To do | |

## Titles

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/titles` | ⏳ To do | |
| GET | `/users/{user_id}/titles` | ⏳ To do | |
| GET | `/titles/{id}` | ⏳ To do | |
| POST | `/titles` | ⏳ To do | |
| PATCH | `/titles/{id}` | ⏳ To do | |
| PUT | `/titles/{id}` | ⏳ To do | |
| DELETE | `/titles/{id}` | ⏳ To do | |

## Titles users

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/titles/{title_id}/titles_users` | ⏳ To do | |
| GET | `/users/{user_id}/titles_users` | ⏳ To do | |
| GET | `/titles_users` | ⏳ To do | |
| GET | `/titles_users/{id}` | ⏳ To do | |
| POST | `/titles_users` | ⏳ To do | |
| PATCH | `/titles_users/{id}` | ⏳ To do | |
| PUT | `/titles_users/{id}` | ⏳ To do | |
| DELETE | `/titles_users/{id}` | ⏳ To do | |

## Transactions

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/transactions` | ⏳ To do | |
| GET | `/users/{user_id}/transactions` | ⏳ To do | |
| GET | `/transactions/{id}` | ⏳ To do | |
| POST | `/transactions` | ⏳ To do | |
| DELETE | `/transactions/{id}` | ⏳ To do | |

## Translations

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/translations` | ⏳ To do | |
| GET | `/translations/{id}/` | ⏳ To do | |
| POST | `/translations` | ⏳ To do | |
| PATCH | `/translations/{id}` | ⏳ To do | |
| PUT | `/translations/{id}` | ⏳ To do | |
| DELETE | `/translations/{id}` | ⏳ To do | |
| POST | `/translations/upload` | ⏳ To do | |


## User candidatures

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/users/{id}/user_candidature` | 🚧 In progress | |
| GET | `/user_candidatures` | ⏳ To do | |
| GET | `/user_candidatures/{id}`| ⏳ To do | |
| POST | `/users/{user_id}/user_candidature` | ⏳ To do | |
| POST | `/user_candidatures` | ⏳ To do | |
| PATCH | `/users/{user_id}/user_candidature` | ⏳ To do | |
| PUT | `/users/{user_id}/user_candidature` | ⏳ To do | |
| PATCH | `/user_candidatures/{id}` | ⏳ To do | |
| PUT | `/user_candidatures/{id}` | ⏳ To do | |

## Users

| Method | Path | Status | Notes |
|---|---|---|---|
| POST | `/users/{id}/correction_points/add` | ⏳ To do | |
| DELETE | `/users/{id}/correction_points/remove` | ⏳ To do | |
| GET | `/users/{id}/locations_stats` | ⏳ To do | |
| GET | `/users/{id}/exam` | ⏳ To do | |
| GET | `/coalitions/{coalition_id}/users` | 🚧 In progress | |
| GET | `/dashes/{dash_id}/users` | ⏳ To do | |
| GET | `/events/{event_id}/users` | ⏳ To do | |
| GET | `/accreditations/{accreditation_id}/users` | 🚧 In progress | |
| GET | `/teams/{team_id}/users` | ⏳ To do | |
| GET | `/projects/{project_id}/users` | 🚧 In progress | |
| GET | `/partnerships/{partnership_id}/users` | 🚧 In progress | |
| GET | `/expertises/{expertise_id}/users` | 🚧 In progress | |
| GET | `/users` | 🚧 In progress | |
| GET | `/cursus/{cursus_id}/users` | 🚧 In progress | |
| GET | `/campus/{campus_id}/users` | 🚧 In progress | |
| GET | `/achievements/{achievement_id}/users` | 🚧 In progress | |
| GET | `/titles/{title_id}/users` | 🚧 In progress | |
| GET | `/quests/{quest_id}/users` | 🚧 In progress | |
| GET | `/groups/{group_id}/users` | ⏳ To do | |
| GET | `/users/{id}` | ✅ Done | Tested with staff, student, anonymized and test accounts |
| POST | `/users` | ⏳ To do | |
| PATCH | `/users/{id}` | ⏳ To do | |
| PUT | `/users/{id}` | ⏳ To do | |
| GET | `/me` | ⏳ To do | |
| POST | `/users/{id}/free_past_agu` | ⏳ To do | |
| POST | `/users/{user_id}/unfreeze` | ⏳ To do | |
| POST | `/users/{id}/set_primary_campus` | ⏳ To do | |
| POST | `/users/{id}/alumnize` | ⏳ To do | |
| POST | `/users/{id}/dealumnize` | ⏳ To do | |
| DELETE | `/users/{id}/otp_settings/remove` | ⏳ To do | |
| GET | `/staff` | ⏳ To do | |
| GET | `/users/{user_id}/projects_users/registration` | ⏳ To do | |

## Waitlists

| Method | Path | Status | Notes |
|---|---|---|---|
| GET | `/waitlists` | ⏳ To do | |
| GET | `/events/{event_id}/waitlist` | ⏳ To do | |
| GET | `/exams/{exam_id}/waitlist` | ⏳ To do | |
| GET | `/waitlists/{id}` | ⏳ To do | |
| DELETE | `/waitlists/{id}` | ⏳ To do | |

## Webhook registeries

| Method | Path | Status | Notes |
|---|---|---|---|
| POST | `/webhook_registeries/{id}/deactivate` | ⏳ To do | |
