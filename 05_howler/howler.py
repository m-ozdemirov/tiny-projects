#!/usr/bin/env python3
'''Howler from Harry Potter'''

import argparse
import os

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()

def main():
    '''Protag theme starts playing'''

    args = get_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf=8') as filename:
            output = filename.read()
    else:
        output = args.text

    if args.outfile:
        with open(args.outfile, 'wt', encoding='utf=8') as out_fh:
            out_fh.write(args.text.upper())
    else:
        print(output.upper())

if __name__ == '__main__':
    main()
