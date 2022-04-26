#!/usr/bin/env python3
'''Telephone'''

import argparse
import os
import random
import string

def get_args():
    '''Getting command-line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('text',
                        metavar='text',
                        help='Text or file')

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        default=None,
                        type=int,
                        help='Random seed (default: None)')

    parser.add_argument('-m',
                        '--mutations',
                        metavar='mutations',
                        default=0.1,
                        type=float,
                        help='Percent mutations (default: 0.1)')

    args = parser.parse_args()

    if args.mutations > 1 or args.mutations < 0:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args

def main():
    '''Protag theme starts playing'''
    args = get_args()
    mutations = args.mutations
    random.seed(args.seed)

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as text:
            text = text.read().rstrip()
    else:
        text = args.text

    alpha = ''.join(sorted(string.punctuation + string.ascii_letters))
    len_text = len(text)
    num_mutations = round(len_text * mutations)
    new_text = list(text)

    for i in random.sample(range(len_text), num_mutations):
        new_text[i] = random.choice(alpha.replace(new_text[i], ''))

    new_text = ''.join(new_text)
    print(f'You said: "{text}"\nI heard: "{new_text}"')

if __name__ == '__main__':
    main()
