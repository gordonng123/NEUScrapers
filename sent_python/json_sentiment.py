"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
import json

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types







    #document = types.Document(
    #    content=content,
    #    type=enums.Document.Type.PLAIN_TEXT)
    # annotations = client.analyze_sentiment(document=document)

    # print(document)
   

    #debug 
   # print(annotations)

    # Print the results
   # print_result(annotations)


if __name__ == '__main__':
   with open('reviews/exp.json') as f:
        data = json.load(f)

        print(data)