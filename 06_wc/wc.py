#!/usr/bin/env python3
'''Word count'''

import argparse
import sys

def get_args():
    '''Get command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('file',
                        metavar='file',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()

def main():
    '''Protag theme starts playing'''

    args = get_args().file

    total_lines, total_bytes, total_words = 0, 0, 0
    for file_handle in args:
        num_lines, num_words, num_bytes = 0, 0, 0
        for line in file_handle:
            num_lines += 1
            num_bytes += len(line)
            num_words += len(line.split())

        total_lines += num_lines
        total_bytes += num_bytes
        total_words += num_words

        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {file_handle.name}')

    if len(args) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')

if __name__ == '__main__':
    main()
