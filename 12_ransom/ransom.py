#!/usr/bin/env python3
'''Ransom note'''

import argparse
import random
import os

def get_args():
    '''Getting command-line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('text',
                        metavar='text',
                        help='input string or file')

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        type=int,
                        default=None,
                        help='random seed (default: None)')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as args.text:
            args.text = args.text.read().rstrip()

    return args

def choose(char):
    '''Randomly return upper or lowercase letter to return'''
    return char.upper() if random.choice([0, 1]) else char.lower()


def main():
    '''Protag theme starts playing'''

    args = get_args()
    text = args.text
    random.seed(args.seed)
    ransom = []
    for i in text:
        ransom.append(choose(i))
    print(''.join(ransom))

if __name__ == '__main__':
    main()
