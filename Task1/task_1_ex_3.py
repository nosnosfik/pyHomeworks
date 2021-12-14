""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Number = Digit{Digit}
Sign = '+' | '-'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = '-123' result = (False, None)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
SIGN = ['+', '-']
global calculate_result


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='Perform mathematical, logical and comparison operations')
    parser.add_argument('user_input', help='Data to check')
    return parser.parse_args()


def check_formula(user_input):
    """ Check 'formula' according EBNF syntax and if it matches calculates result """
    global calculate_result
    match_result = True
    check_string = ''
    for char in user_input:
        if char.isdigit() or char in SIGN:
            if len(check_string) == 0 and (char not in DIGITS or char in SIGN):  # The first character check
                match_result = False
                break
            if len(check_string) > 0 and check_string[-1] in SIGN and char in SIGN:  # Sign duplicates check
                match_result = False
                break
            check_string += char
        else:
            match_result = False
            break
    if match_result:
        exec(f'global calculate_result; calculate_result = {check_string}')
    else:
        calculate_result = None
    result = match_result, calculate_result
    return result


def main():
    args = get_args()  # Hint: use methods from argparse module
    print(check_formula(args.user_input))


if __name__ == '__main__':
    main()
