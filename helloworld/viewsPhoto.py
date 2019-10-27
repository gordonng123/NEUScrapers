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

import io
import os

from django.http import HttpResponse

from igramscraper.instagram import Instagram  # pylint: disable=no-name-in-module

from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import storage
from google.cloud import vision
from google.cloud.vision import types

from google.cloud import bigquery


import datetime

def index(request):
    return HttpResponse(
        'Hello, World. This is Django running on Google App Engine')


def scrape(request):
    sc()
    return HttpResponse(
        'Hello, World. This is Django running on Google App Engine')

def detect_logos_uri(uri):
    """Detects logos in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    return logos

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts

def sc():
    instagram = Instagram()
    # instagram.with_credentials('username', 'password', 'path/to/cache/folder')
    # instagram.login()
    proxies = {
        'https': 'http://124.41.213.211',
        'https': 'http://217.64.109.231',
    }

    medias = instagram.get_medias_by_tag('flying', count=1000)

    instagram.set_proxies(proxies)
    data = []
    for media in medias:
        if (media.type == 'image'):
            flag = False
            url = media.image_high_resolution_url
            logos = detect_logos_uri(url)
            texts = detect_text_uri(url)
            for logo in logos:
                logoN = logo.description.lower()
                if((logoN == 'delta air lines') or (logoN == 'jetblue') or (logoN == 'southwest airlines')):
                    flag = True
                    print(logoN)
            for text in texts:
                comp = text.description.lower()
                if((comp == 'delta') or (comp == 'jetblue') or (comp == 'southwest')):
                    flag = True
                    print(comp)
            if (flag):
                data.append((media.created_time, media.caption, location_name))

        # textArray.append(media.caption)
        # data_things = {data}
        # sample_analyze_sentiment(media.caption, data[-1])

    """
    table_id = "test"
    bt_client = bigtable.Client(project='yaleproject', admin=True)
    instance = bt_client.instance('instagram-jetblue')

    print('Creating the {} table.'.format(table_id))
    table = instance.table(table_id)

    print('Creating column family cf1 with Max Version GC rule...')

    max_versions_rule = column_family.MaxVersionsGCRule(2)
    column_family_id = 'cf1'
    column_families = {column_family_id: max_versions_rule}
    if not table.exists():
        table.create(column_families=column_families)
    else:
        print("Table {} already exists.".format(table_id))

    print('Writing some greetings to the table.')
    greetings = ['Hello World!', 'Hello Cloud Bigtable!', 'Hello Python!']
    rows = []
    column = 'greeting'.encode()
    for i in range(1, 100000):
        row_key = 'greeting{}'.format(i).encode()
        row = table.row(row_key)
        row.set_cell(column_family_id,
                     column,
                     'Hello World!{}'.format(i),
                     timestamp=datetime.datetime.utcnow())
        rows.append(row)
    table.mutate_rows(rows)

    row_filter = row_filters.CellsColumnLimitFilter(1)

    print('Scanning for all greetings:')
    partial_rows = table.read_rows(filter_=row_filter)

    counter = 0
    for row in partial_rows:
        cell = row.cells[column_family_id][column][0]
        print(cell.value.decode('utf-8'))
""" 
    bq_client = bigquery.Client()
    print(data)
    dataset_id = 'vacationDataset'  # replace with your dataset ID
    # For this sample, the table must already exist and have a defined schema
    table_id = 'list'  # replace with your table ID
    table_ref = bq_client.dataset(dataset_id).table(table_id)
    table = bq_client.get_table(table_ref)  # API request

    errors = bq_client.insert_rows(table, data)  # API request

    assert errors == []
    
def test():
    instagram = Instagram()
    # instagram.with_credentials('username', 'password', 'path/to/cache/folder')
    # instagram.login()
    proxies = {
        'https': 'http://124.41.213.211',
        'https': 'http://217.64.109.231',
    }

    medias = instagram.get_medias_by_tag('vacation', count=1000)
    print(medias[0].type)

def sample_analyze_sentiment(text_content, array_name):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    l_client = language_v1.LanguageServiceClient()


    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = l_client.analyze_sentiment(document, encoding_type=encoding_type)
    # Get overall sentiment of the input document
    print(u"Document sentiment score: {}".format(
        response.document_sentiment.score))
    array_name["sentiments"] = format(response.document_sentiment.score)
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

    print(u"Language of the text: {}".format(response.language))

sc()