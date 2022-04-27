#!/usr/bin/env python3
'''Bottles of beer song'''

import argparse

def get_args():
    '''Getting command-line arguments'''

    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--num',
                        metavar='number',
                        type=int,
                        default=10,
                        help='how many bottles (default: 10)')

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args

def verse(bottles):
    '''Sing a verse'''

    next_bottle = bottles -1
    s1 = '' if bottles == 1 else 's'
    s2 = '' if next_bottle == 1 else 's'
    num_next = 'No more' if next_bottle == 0 else next_bottle

    return '\n'.join([
        f'{bottles} bottle{s1} of beer on the wall,',
        f'{bottles} bottle{s1} of beer,',
        'Take one down, pass it around,',
        f'{num_next} bottle{s2} of beer on the wall!',
    ])


def main():
    '''Protag theme starts playing'''

    number = get_args().num
    print('\n\n'.join(map(verse, range(number, 0, -1))))


if __name__ == '__main__':
    main()
