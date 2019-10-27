"""Demonstrates how to make a simple call to the Natural Language API."""

import argparse
import io
import json
import os


import numpy
import six

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types




def analyze(path, index_file):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()
    
    result ={}

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if not os.path.isfile(file_path):
            continue 

        try: 
            with io.open(file_path, 'r') as f: 

                #debug
                 text = f.read()
                 print(text)
                 annotations = client.analyze_sentiment(text)
                 
                 #Debug
                 print(annotations)

                 result[filename] = annotations
        except Exception:
            print('Failed to process {}'.format(file_path))
    #debug
    print(type(result))

    with io.open(index_file, 'w', encoding='utf-8') as d:
        d.write(unicode(json.dumps(result, ensure_ascii=False)))

    print('Texts indexed in file: {}'.format(index_file))
    return result
          

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')
    index_parser = subparsers.add_parser(
        'analyze', help='lol')
    index_parser.add_argument(
        'path', help='The directory that contains '
        'text files to be indexed.')
    index_parser.add_argument(
        '--index_file', help='Filename for the output JSON.',
        default='index.json')
    args = parser.parse_args()

    analyze(args.path, args.index_file)