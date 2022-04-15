#!/usr/bin/env python3
'''Gahlycrumb'''

import argparse

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('--file',
                        '-f',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()

def main():
    '''Protag theme starts palying'''

    args = get_args()
    letters = args.letter

    tf_dict = {}

    for line in args.file:
        tf_dict[line[0]] = line.rstrip()

    for letter in letters:
        if letter.upper() in tf_dict.keys():
            print(tf_dict[letter.upper()])
        else:
            print(f'I do not know "{letter}".')

if __name__ == '__main__':
    main()
