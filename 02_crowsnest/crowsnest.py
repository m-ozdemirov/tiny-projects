#!/usr/bin/env python3
'''Crow\'s Nest'''

import argparse

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='a word')

    return parser.parse_args()

def main():
    '''Protag theme starts playing'''
    args = get_args()
    word = args.word

    if word[0] in 'aeiouAEIUO':
        print(f'Ahoy, Captain, an {word} off the larboard bow!')
    else:
        print(f'Ahoy, Captain, a {word} off the larboard bow!')

if __name__ == '__main__':
    main()
