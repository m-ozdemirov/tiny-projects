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

def verse(days):
    '''Returns a verse of a song'''

    days_dict = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth',
                 5: 'fifth', 6: 'sixth', 7: 'seventh', 8: 'eighth',
                 9: 'nineth', 10: 'tenth', 11: 'eleventh', 12: 'twelvth'}

    gifts = ['A partridge in a pear tree', 'Two turtle doves', 'Three French hens',
             'Four callling birds', 'Five gold rings', 'Six geese a laying',
             'Seven swans a swimming', 'Eight maids a milking', 'Nine ladies dancing',
             'Ten lords a leaping', 'Eleven pipers piping', 'Twelve drummers drumming']

    gifts_sliced = list(reversed(gifts[:days]))

    last_line = 'A partridge in a pear tree.' if days == 1 else 'And a partridge in a pear tree.'
    new_line = '\n'

    if days == 1:
        main_lines = ''
    else:
        main_lines = f'{new_line.join(gifts_sliced[:-1])},\n'

    return ''.join([f'On the {days_dict[days]} day of Christmas,\n',
                   f'My true love gave to me,\n',
                   f'{main_lines}',
                   f'{last_line}\n'])

def main():
    '''Protag theme starts playing'''

    args = get_args()

    for i in range(1, args.num+1):
        if i != args.num:
            print(verse(i), file=args.outfile)
        else:
            print(verse(i).rstrip(), file=args.outfile)

if __name__ == '__main__':
    main()
