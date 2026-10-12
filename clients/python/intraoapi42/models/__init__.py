"""Contains all the data models used in inputs/outputs"""

from .accreditation import Accreditation
from .achievement import Achievement
from .bloc import Bloc
from .campus import Campus
from .campus_user import CampusUser
from .coalition import Coalition
from .coalitions_user import CoalitionsUser
from .cursus import Cursus
from .cursus_user import CursusUser
from .error import Error
from .event import Event
from .event_themes_item import EventThemesItem
from .event_waitlist_type_0 import EventWaitlistType0
from .events_user import EventsUser
from .events_user_event import EventsUserEvent
from .expertise import Expertise
from .expertises_user import ExpertisesUser
from .get_accreditations_filter import GetAccreditationsFilter
from .get_accreditations_range import GetAccreditationsRange
from .get_closes_by_user_id_filter import GetClosesByUserIdFilter
from .get_closes_by_user_id_range import GetClosesByUserIdRange
from .get_closes_filter import GetClosesFilter
from .get_closes_range import GetClosesRange
from .get_internships_by_user_id_filter import GetInternshipsByUserIdFilter
from .get_internships_by_user_id_range import GetInternshipsByUserIdRange
from .get_internships_filter import GetInternshipsFilter
from .get_internships_range import GetInternshipsRange
from .get_language_by_id_filter import GetLanguageByIdFilter
from .get_language_by_id_range import GetLanguageByIdRange
from .get_notes_by_user_id_filter import GetNotesByUserIdFilter
from .get_notes_by_user_id_range import GetNotesByUserIdRange
from .get_projects_users_by_project_id_filter import GetProjectsUsersByProjectIdFilter
from .get_projects_users_by_project_id_range import GetProjectsUsersByProjectIdRange
from .get_projects_users_by_user_id_filter import GetProjectsUsersByUserIdFilter
from .get_projects_users_by_user_id_range import GetProjectsUsersByUserIdRange
from .get_projects_users_filter import GetProjectsUsersFilter
from .get_projects_users_range import GetProjectsUsersRange
from .get_teams_by_me_filter import GetTeamsByMeFilter
from .get_teams_by_me_range import GetTeamsByMeRange
from .get_teams_by_project_id_filter import GetTeamsByProjectIdFilter
from .get_teams_by_project_id_range import GetTeamsByProjectIdRange
from .get_teams_by_project_session_id_filter import GetTeamsByProjectSessionIdFilter
from .get_teams_by_project_session_id_range import GetTeamsByProjectSessionIdRange
from .get_teams_by_user_id_and_project_id_filter import GetTeamsByUserIdAndProjectIdFilter
from .get_teams_by_user_id_and_project_id_range import GetTeamsByUserIdAndProjectIdRange
from .get_teams_by_user_id_filter import GetTeamsByUserIdFilter
from .get_teams_by_user_id_range import GetTeamsByUserIdRange
from .get_teams_filter import GetTeamsFilter
from .get_teams_range import GetTeamsRange
from .get_users_by_accreditation_id_filter import GetUsersByAccreditationIdFilter
from .get_users_by_accreditation_id_range import GetUsersByAccreditationIdRange
from .get_users_by_achievement_filter import GetUsersByAchievementFilter
from .get_users_by_achievement_range import GetUsersByAchievementRange
from .get_users_by_campus_filter import GetUsersByCampusFilter
from .get_users_by_campus_range import GetUsersByCampusRange
from .get_users_by_coalition_id_filter import GetUsersByCoalitionIdFilter
from .get_users_by_coalition_id_range import GetUsersByCoalitionIdRange
from .get_users_by_cursus_filter import GetUsersByCursusFilter
from .get_users_by_cursus_range import GetUsersByCursusRange
from .get_users_by_expertise_id_filter import GetUsersByExpertiseIdFilter
from .get_users_by_expertise_id_range import GetUsersByExpertiseIdRange
from .get_users_by_partnership_id_filter import GetUsersByPartnershipIdFilter
from .get_users_by_partnership_id_range import GetUsersByPartnershipIdRange
from .get_users_by_project_id_filter import GetUsersByProjectIdFilter
from .get_users_by_project_id_range import GetUsersByProjectIdRange
from .get_users_by_quest_filter import GetUsersByQuestFilter
from .get_users_by_quest_range import GetUsersByQuestRange
from .get_users_by_title_filter import GetUsersByTitleFilter
from .get_users_by_title_range import GetUsersByTitleRange
from .get_users_filter import GetUsersFilter
from .get_users_range import GetUsersRange
from .group import Group
from .groups_user import GroupsUser
from .internship import Internship
from .internship_convention import InternshipConvention
from .internship_convention_convention import InternshipConventionConvention
from .language import Language
from .language_user import LanguageUser
from .light_achievements_user import LightAchievementsUser
from .light_app import LightApp
from .light_campus import LightCampus
from .light_close import LightClose
from .light_close_kind import LightCloseKind
from .light_close_state import LightCloseState
from .light_community_service import LightCommunityService
from .light_community_service_state import LightCommunityServiceState
from .light_note import LightNote
from .light_note_user import LightNoteUser
from .light_project import LightProject
from .light_project_user import LightProjectUser
from .light_team import LightTeam
from .light_team_user import LightTeamUser
from .light_user import LightUser
from .light_user_kind import LightUserKind
from .location import Location
from .patch_project_user_by_id_body import PatchProjectUserByIdBody
from .patch_team_by_id_body import PatchTeamByIdBody
from .patronage import Patronage
from .post_projects_users_body import PostProjectsUsersBody
from .project import Project
from .project_project_statistics import ProjectProjectStatistics
from .project_tags_item import ProjectTagsItem
from .project_user import ProjectUser
from .project_user_create import ProjectUserCreate
from .project_user_update import ProjectUserUpdate
from .put_project_user_by_id_body import PutProjectUserByIdBody
from .put_team_by_id_body import PutTeamByIdBody
from .question_answer import QuestionAnswer
from .question_with_answers import QuestionWithAnswers
from .role import Role
from .scale_flag import ScaleFlag
from .scale_team import ScaleTeam
from .scale_team_truant import ScaleTeamTruant
from .scale_user import ScaleUser
from .skill import Skill
from .slot import Slot
from .slot_create import SlotCreate
from .slot_create_slot import SlotCreateSlot
from .team import Team
from .team_update import TeamUpdate
from .team_update_teams_users_attributes_type_0_item import TeamUpdateTeamsUsersAttributesType0Item
from .team_upload import TeamUpload
from .title import Title
from .title_user import TitleUser
from .translation import Translation
from .translation_fields import TranslationFields
from .user import User
from .user_candidature import UserCandidature
from .user_candidature_gender import UserCandidatureGender
from .user_image import UserImage
from .user_image_versions import UserImageVersions
from .user_preview import UserPreview

__all__ = (
    "Accreditation",
    "Achievement",
    "Bloc",
    "Campus",
    "CampusUser",
    "Coalition",
    "CoalitionsUser",
    "Cursus",
    "CursusUser",
    "Error",
    "Event",
    "EventsUser",
    "EventsUserEvent",
    "EventThemesItem",
    "EventWaitlistType0",
    "Expertise",
    "ExpertisesUser",
    "GetAccreditationsFilter",
    "GetAccreditationsRange",
    "GetClosesByUserIdFilter",
    "GetClosesByUserIdRange",
    "GetClosesFilter",
    "GetClosesRange",
    "GetInternshipsByUserIdFilter",
    "GetInternshipsByUserIdRange",
    "GetInternshipsFilter",
    "GetInternshipsRange",
    "GetLanguageByIdFilter",
    "GetLanguageByIdRange",
    "GetNotesByUserIdFilter",
    "GetNotesByUserIdRange",
    "GetProjectsUsersByProjectIdFilter",
    "GetProjectsUsersByProjectIdRange",
    "GetProjectsUsersByUserIdFilter",
    "GetProjectsUsersByUserIdRange",
    "GetProjectsUsersFilter",
    "GetProjectsUsersRange",
    "GetTeamsByMeFilter",
    "GetTeamsByMeRange",
    "GetTeamsByProjectIdFilter",
    "GetTeamsByProjectIdRange",
    "GetTeamsByProjectSessionIdFilter",
    "GetTeamsByProjectSessionIdRange",
    "GetTeamsByUserIdAndProjectIdFilter",
    "GetTeamsByUserIdAndProjectIdRange",
    "GetTeamsByUserIdFilter",
    "GetTeamsByUserIdRange",
    "GetTeamsFilter",
    "GetTeamsRange",
    "GetUsersByAccreditationIdFilter",
    "GetUsersByAccreditationIdRange",
    "GetUsersByAchievementFilter",
    "GetUsersByAchievementRange",
    "GetUsersByCampusFilter",
    "GetUsersByCampusRange",
    "GetUsersByCoalitionIdFilter",
    "GetUsersByCoalitionIdRange",
    "GetUsersByCursusFilter",
    "GetUsersByCursusRange",
    "GetUsersByExpertiseIdFilter",
    "GetUsersByExpertiseIdRange",
    "GetUsersByPartnershipIdFilter",
    "GetUsersByPartnershipIdRange",
    "GetUsersByProjectIdFilter",
    "GetUsersByProjectIdRange",
    "GetUsersByQuestFilter",
    "GetUsersByQuestRange",
    "GetUsersByTitleFilter",
    "GetUsersByTitleRange",
    "GetUsersFilter",
    "GetUsersRange",
    "Group",
    "GroupsUser",
    "Internship",
    "InternshipConvention",
    "InternshipConventionConvention",
    "Language",
    "LanguageUser",
    "LightAchievementsUser",
    "LightApp",
    "LightCampus",
    "LightClose",
    "LightCloseKind",
    "LightCloseState",
    "LightCommunityService",
    "LightCommunityServiceState",
    "LightNote",
    "LightNoteUser",
    "LightProject",
    "LightProjectUser",
    "LightTeam",
    "LightTeamUser",
    "LightUser",
    "LightUserKind",
    "Location",
    "PatchProjectUserByIdBody",
    "PatchTeamByIdBody",
    "Patronage",
    "PostProjectsUsersBody",
    "Project",
    "ProjectProjectStatistics",
    "ProjectTagsItem",
    "ProjectUser",
    "ProjectUserCreate",
    "ProjectUserUpdate",
    "PutProjectUserByIdBody",
    "PutTeamByIdBody",
    "QuestionAnswer",
    "QuestionWithAnswers",
    "Role",
    "ScaleFlag",
    "ScaleTeam",
    "ScaleTeamTruant",
    "ScaleUser",
    "Skill",
    "Slot",
    "SlotCreate",
    "SlotCreateSlot",
    "Team",
    "TeamUpdate",
    "TeamUpdateTeamsUsersAttributesType0Item",
    "TeamUpload",
    "Title",
    "TitleUser",
    "Translation",
    "TranslationFields",
    "User",
    "UserCandidature",
    "UserCandidatureGender",
    "UserImage",
    "UserImageVersions",
    "UserPreview",
)
