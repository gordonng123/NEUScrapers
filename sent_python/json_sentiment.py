"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
import json

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums


def sample_analyze_sentiment(text_content, itemname):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

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
    distro["sentiments"] = format(response.document_sentiment.score)
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


if __name__ == '__main__':
    # ../data/jetblue_parsed.json
    # reviews/exp.json
    with open('../data/jetblue_parsed.json') as f:
        data = json.load(f)
        print(data)

    for distro in data['items']:
        x = distro['text']
        # print(x)

        sample_analyze_sentiment(x, distro)

with open('newout.json', 'w') as out:
    json.dump(data, out)
