#!/usr/bin/env python3
'''Twelve days of Christmas'''

import argparse
import sys

def get_args():
    '''Getting command-line arguments'''

    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--num',
                        metavar='days',
                        type=int,
                        default=12,
                        help='Number of days to sing (defaults: 12)')

    parser.add_argument('-o', '--outfile',
                        metavar='FILE',
                        help='Save output in a file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()

    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args

def verse(day):
    '''Returns a verse of a song'''

    days_dict = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth',
                 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth',
                 9: 'nineth', 10: 'tenth', 11: 'eleventh', 12: 'twelvth'}

    gifts = ['A partridge in a pear tree.', 'Two turtle doves', 'Three French hens',
             'Four callling birds', 'Five gold rings', 'Six geese a laying',
             'Seven swans a swimming', 'Eight maids a milking', 'Nine ladies dancing',
             'Ten lords a leaping', 'Eleven pipers piping', 'Twelve drummers drumming']

    lines = [f'On the {days_dict[day]} day of Christmas',
             'My true love gave to me']

    lines.extend(reversed(gifts[:day]))

    if day > 1:
        lines[-1] = f'And {lines[-1].lower()}'

    return ',\n'.join(lines)

def main():
    '''Protag theme starts playing'''

    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    print('\n\n'.join(verses), file=args.outfile)

if __name__ == '__main__':
    main()
