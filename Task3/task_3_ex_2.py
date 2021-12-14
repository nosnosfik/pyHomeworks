"""
Write a function converting a Roman numeral from a given string N into an Arabic numeral.
Values may range from 1 to 100 and may contain invalid symbols.
Invalid symbols and numerals out of range should raise ValueError.

Numeral / Value:
I: 1
V: 5
X: 10
L: 50
C: 100

Example:
N = 'I'; result = 1
N = 'XIV'; result = 14
N = 'LXIV'; result = 64

Example of how the task should be called:
python3 task_3_ex_2.py LXIV

Note: use `argparse` module to parse passed CLI arguments
"""
import argparse

NUMERALS = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100}


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='Converts a Roman numeral from a given string into an Arabic numeral')
    parser.add_argument('numeral', type=str, help='Input roman numeral')
    return parser.parse_args()


def from_roman_numerals(args):
    """Converts from roman numeral to arabic"""
    if args is None:
        args = get_args()
    arabic_way = 0
    tmp = 0
    for num in args.numeral:
        if num not in NUMERALS:
            raise ValueError('Entered data is incorrect')
        if NUMERALS.get(num) > tmp:
            arabic_way += NUMERALS.get(num) - 2 * tmp
        else:
            arabic_way += NUMERALS.get(num)
        tmp = NUMERALS.get(num)
    return arabic_way


def main():
    args = None
    print(from_roman_numerals(args))


if __name__ == "__main__":
    main()
