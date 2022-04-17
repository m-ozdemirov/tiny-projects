#!/usr/bin/env python3
'''Apples and bananas'''

import argparse
import os

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('file',
                        metavar='file',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute (default: a)',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices='aeiou')

    return parser.parse_args()

def main():
    '''Protag theme starts playing'''

    args = get_args()

    if os.path.isfile(args.file):
        with open(args.file, encoding='utf-8') as text:
            text = text.read().rstrip()
    else:
        text = args.file

    modified = ''
    for char in text:
        if char in 'aeiou':
            modified += args.vowel
        elif char in 'AEIOU':
            modified += args.vowel.upper()
        else:
            modified += char

    print(modified)

if __name__ == '__main__':
    main()
