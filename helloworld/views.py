#!/usr/bin/env python
# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import instagram_scraper as insta
import json
from subprocess import call
from django.http import HttpResponse
import subprocess
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import storage
from igramscraper.instagram import Instagram  # pylint: disable=no-name-in-module
from google.oauth2 import service_account

def index(request):
    return HttpResponse(
        'Hello, World. This is Django running on Google App Engine')


def scrape(request):
    sc()
    return HttpResponse(
        'Hello, World. This is Django running on Google App Engine')


def sc():
    instagram = Instagram()
    # instagram.with_credentials('username', 'password', 'path/to/cache/folder')
    # instagram.login()
    proxies = {
        'http': 'http://123.45.67.8:1087',
        'https': 'http://123.45.67.8:1087',
    }

    medias = instagram.get_medias_by_tag('jetblue', count=20)

    # for media in medias:
    #    print(media)
    ###   account = media.owner
    #   print('Id', account.identifier)
    # print('Username', account.username)
    # print('Full Name', account.full_name)
    # print('Profile Pic Url', account.get_profile_picture_url_hd())
    #   print('--------------------------------------------------')
    data = []
    textArray = []
    for media in medias:
        data.append({"time": media.created_time, "text": media.caption})
        # textArray.append(media.caption)
        # data_things = {data}
        sample_analyze_sentiment(media.caption, data[-1])


def sample_analyze_sentiment(text_content, arrayName):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    storage_client = storage.Client.from_service_account_json(
        'YaleProject-d4b4a18b7f6e.json')

    client = language_v1.LanguageServiceClient().from_service_account_json(
        'YaleProject-d4b4a18b7f6e.json')

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(
        response.document_sentiment.score))
    arrayName["sentiments"] = format(response.document_sentiment.score)
    print(
        u"Document sentiment magnitude: {}".format(
            response.document_sentiment.magnitude
        )
    )
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(u"Sentence text: {}".format(sentence.text.content))
        print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        print(u"Sentence sentiment magnitude: {}".format(
            sentence.sentiment.magnitude))

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

    # document = types.Document(
    #    content=content,
    #    type=enums.Document.Type.PLAIN_TEXT)
    # annotations = client.analyze_sentiment(document=document)

    # print(document)
