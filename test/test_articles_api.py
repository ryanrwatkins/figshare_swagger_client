# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.articles_api import ArticlesApi


class TestArticlesApi(unittest.TestCase):
    """ ArticlesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.articles_api.ArticlesApi()

    def tearDown(self):
        pass

    def test_account_article_report(self):
        """
        Test case for account_article_report

        Account Article Report
        """
        pass

    def test_account_article_report_generate(self):
        """
        Test case for account_article_report_generate

        Initiate a new Report
        """
        pass

    def test_article_details(self):
        """
        Test case for article_details

        View article details
        """
        pass

    def test_article_file_details(self):
        """
        Test case for article_file_details

        Article file details
        """
        pass

    def test_article_files(self):
        """
        Test case for article_files

        List article files
        """
        pass

    def test_article_version_confidentiality(self):
        """
        Test case for article_version_confidentiality

        Public Article Confidentiality for article version
        """
        pass

    def test_article_version_details(self):
        """
        Test case for article_version_details

        Article details for version
        """
        pass

    def test_article_version_embargo(self):
        """
        Test case for article_version_embargo

        Public Article Embargo for article version
        """
        pass

    def test_article_version_update(self):
        """
        Test case for article_version_update

        Update article version
        """
        pass

    def test_article_version_update_thumb(self):
        """
        Test case for article_version_update_thumb

        Update article version thumbnail
        """
        pass

    def test_article_versions(self):
        """
        Test case for article_versions

        List article versions
        """
        pass

    def test_articles_list(self):
        """
        Test case for articles_list

        Public Articles
        """
        pass

    def test_articles_search(self):
        """
        Test case for articles_search

        Public Articles Search
        """
        pass

    def test_private_article_author_delete(self):
        """
        Test case for private_article_author_delete

        Delete article author
        """
        pass

    def test_private_article_authors_add(self):
        """
        Test case for private_article_authors_add

        Add article authors
        """
        pass

    def test_private_article_authors_list(self):
        """
        Test case for private_article_authors_list

        List article authors
        """
        pass

    def test_private_article_authors_replace(self):
        """
        Test case for private_article_authors_replace

        Replace article authors
        """
        pass

    def test_private_article_categories_add(self):
        """
        Test case for private_article_categories_add

        Add article categories
        """
        pass

    def test_private_article_categories_list(self):
        """
        Test case for private_article_categories_list

        List article categories
        """
        pass

    def test_private_article_categories_replace(self):
        """
        Test case for private_article_categories_replace

        Replace article categories
        """
        pass

    def test_private_article_category_delete(self):
        """
        Test case for private_article_category_delete

        Delete article category
        """
        pass

    def test_private_article_confidentiality_delete(self):
        """
        Test case for private_article_confidentiality_delete

        Delete article confidentiality
        """
        pass

    def test_private_article_confidentiality_details(self):
        """
        Test case for private_article_confidentiality_details

        Article confidentiality details
        """
        pass

    def test_private_article_confidentiality_update(self):
        """
        Test case for private_article_confidentiality_update

        Update article confidentiality
        """
        pass

    def test_private_article_create(self):
        """
        Test case for private_article_create

        Create new Article
        """
        pass

    def test_private_article_delete(self):
        """
        Test case for private_article_delete

        Delete article
        """
        pass

    def test_private_article_details(self):
        """
        Test case for private_article_details

        Article details
        """
        pass

    def test_private_article_embargo_delete(self):
        """
        Test case for private_article_embargo_delete

        Delete Article Embargo
        """
        pass

    def test_private_article_embargo_details(self):
        """
        Test case for private_article_embargo_details

        Article Embargo Details
        """
        pass

    def test_private_article_embargo_update(self):
        """
        Test case for private_article_embargo_update

        Update Article Embargo
        """
        pass

    def test_private_article_file(self):
        """
        Test case for private_article_file

        Single File
        """
        pass

    def test_private_article_file_delete(self):
        """
        Test case for private_article_file_delete

        File Delete
        """
        pass

    def test_private_article_files_list(self):
        """
        Test case for private_article_files_list

        List article files
        """
        pass

    def test_private_article_private_link(self):
        """
        Test case for private_article_private_link

        List private links
        """
        pass

    def test_private_article_private_link_create(self):
        """
        Test case for private_article_private_link_create

        Create private link
        """
        pass

    def test_private_article_private_link_delete(self):
        """
        Test case for private_article_private_link_delete

        Disable private link
        """
        pass

    def test_private_article_private_link_update(self):
        """
        Test case for private_article_private_link_update

        Update private link
        """
        pass

    def test_private_article_publish(self):
        """
        Test case for private_article_publish

        Private Article Publish
        """
        pass

    def test_private_article_reserve_doi(self):
        """
        Test case for private_article_reserve_doi

        Private Article Reserve DOI
        """
        pass

    def test_private_article_reserve_handle(self):
        """
        Test case for private_article_reserve_handle

        Private Article Reserve Handle
        """
        pass

    def test_private_article_resource(self):
        """
        Test case for private_article_resource

        Private Article Resource
        """
        pass

    def test_private_article_update(self):
        """
        Test case for private_article_update

        Update article
        """
        pass

    def test_private_article_upload_complete(self):
        """
        Test case for private_article_upload_complete

        Complete Upload
        """
        pass

    def test_private_article_upload_initiate(self):
        """
        Test case for private_article_upload_initiate

        Initiate Upload
        """
        pass

    def test_private_articles_list(self):
        """
        Test case for private_articles_list

        Private Articles
        """
        pass

    def test_private_articles_search(self):
        """
        Test case for private_articles_search

        Private Articles search
        """
        pass


if __name__ == '__main__':
    unittest.main()
