#!/usr/bin/env python3
"""tests for twelve_days.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './twelve_days.py'
day_one = '\n'.join([
    'On the first day of Christmas,', 'My true love gave to me,',
    'A partridge in a pear tree.'
])

day_two = '\n'.join([
    'On the second day of Christmas,',
    'My true love gave to me,',
    'Two turtle doves,',
    'And a partridge in a pear tree.'
])


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_num():
    """test bad_num"""

    for n in [random.choice(r) for r in (range(-10, -1), range(13, 20))]:
        rv, out = getstatusoutput(f'{prg} -n {n}')
        assert rv != 0
        assert re.search(f'--num "{n}" must be between 1 and 12', out)


# --------------------------------------------------
def test_one():
    """test one"""

    out = getoutput(f'{prg} -n 1')
    assert out.rstrip() == day_one


# --------------------------------------------------
def test_two():
    """test two"""

    out = getoutput(f'{prg} --num 2')
    assert out == '\n\n'.join([day_one, day_two])


# --------------------------------------------------
def test_all_stdout():
    """test"""

    out = getoutput(f'{prg}').splitlines()
    assert len(out) == 113
    assert out[0] == 'On the first day of Christmas,'
    assert out[-1] == 'And a partridge in a pear tree.'


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
