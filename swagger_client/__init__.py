# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.account import Account
from .models.account_create import AccountCreate
from .models.account_group_roles import AccountGroupRoles
from .models.account_group_roles_create import AccountGroupRolesCreate
from .models.account_report import AccountReport
from .models.account_update import AccountUpdate
from .models.article import Article
from .models.article_confidentiality import ArticleConfidentiality
from .models.article_create import ArticleCreate
from .models.article_doi import ArticleDOI
from .models.article_embargo import ArticleEmbargo
from .models.article_embargo_updater import ArticleEmbargoUpdater
from .models.article_handle import ArticleHandle
from .models.article_project_create import ArticleProjectCreate
from .models.article_update import ArticleUpdate
from .models.article_versions import ArticleVersions
from .models.articles_creator import ArticlesCreator
from .models.author import Author
from .models.authors_creator import AuthorsCreator
from .models.categories_creator import CategoriesCreator
from .models.category import Category
from .models.collaborator import Collaborator
from .models.collection import Collection
from .models.collection_create import CollectionCreate
from .models.collection_doi import CollectionDOI
from .models.collection_handle import CollectionHandle
from .models.collection_private_link_creator import CollectionPrivateLinkCreator
from .models.collection_update import CollectionUpdate
from .models.collection_versions import CollectionVersions
from .models.common_search import CommonSearch
from .models.confidentiality_creator import ConfidentialityCreator
from .models.create_project_response import CreateProjectResponse
from .models.curation import Curation
from .models.curation_comment import CurationComment
from .models.curation_comment_create import CurationCommentCreate
from .models.custom_article_field import CustomArticleField
from .models.custom_article_field_add import CustomArticleFieldAdd
from .models.error_message import ErrorMessage
from .models.file_creator import FileCreator
from .models.file_id import FileId
from .models.funding_create import FundingCreate
from .models.funding_information import FundingInformation
from .models.funding_search import FundingSearch
from .models.group import Group
from .models.group_embargo_options import GroupEmbargoOptions
from .models.institution import Institution
from .models.institution_accounts_search import InstitutionAccountsSearch
from .models.item_type import ItemType
from .models.license import License
from .models.location import Location
from .models.location_warnings import LocationWarnings
from .models.location_warnings_update import LocationWarningsUpdate
from .models.private_authors_search import PrivateAuthorsSearch
from .models.private_link import PrivateLink
from .models.private_link_creator import PrivateLinkCreator
from .models.private_link_response import PrivateLinkResponse
from .models.project import Project
from .models.project_collaborator import ProjectCollaborator
from .models.project_collaborator_invite import ProjectCollaboratorInvite
from .models.project_create import ProjectCreate
from .models.project_note import ProjectNote
from .models.project_note_create import ProjectNoteCreate
from .models.project_update import ProjectUpdate
from .models.public_file import PublicFile
from .models.resource import Resource
from .models.response_message import ResponseMessage
from .models.role import Role
from .models.short_account import ShortAccount
from .models.short_custom_field import ShortCustomField
from .models.timeline_update import TimelineUpdate
from .models.upload_file_part import UploadFilePart
from .models.upload_info import UploadInfo
from .models.user import User
from .models.article_search import ArticleSearch
from .models.article_with_project import ArticleWithProject
from .models.author_complete import AuthorComplete
from .models.collection_complete import CollectionComplete
from .models.collection_complete_private import CollectionCompletePrivate
from .models.collection_search import CollectionSearch
from .models.curation_detail import CurationDetail
from .models.private_file import PrivateFile
from .models.project_article import ProjectArticle
from .models.project_complete import ProjectComplete
from .models.project_note_private import ProjectNotePrivate
from .models.project_private import ProjectPrivate
from .models.projects_search import ProjectsSearch
from .models.timeline import Timeline
from .models.article_complete import ArticleComplete
from .models.private_article_search import PrivateArticleSearch
from .models.private_collection_search import PrivateCollectionSearch
from .models.project_complete_private import ProjectCompletePrivate
from .models.article_complete_private import ArticleCompletePrivate

# import apis into sdk package
from .apis.articles_api import ArticlesApi
from .apis.authors_api import AuthorsApi
from .apis.collections_api import CollectionsApi
from .apis.institutions_api import InstitutionsApi
from .apis.other_api import OtherApi
from .apis.projects_api import ProjectsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
