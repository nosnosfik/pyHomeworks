"""01-Task1-Task1
Write a Python-script that performs simple arithmetic operations: '+', '-', '*', '/'. The type of operator and
data are set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py 1 * 2

Notes:
For other operations need to raise NotImplementedError.
Do not dynamically execute your code (for example, using exec()).
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import argparse
import operator

OPERATORS = ['+', '-', '*', '/']


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='Perform simple arithmetic operations')
    parser.add_argument('operand_1', type=float, help='First operand of expression')
    parser.add_argument('operator', type=str, help='Expression operator')
    parser.add_argument('operand_2', type=float, help='Second operand of expression')
    return parser.parse_args()


def calculate(args):
    """ Calculating expression with data from get_args() function """
    try:
        args = get_args()
        if args.operator not in OPERATORS:
            raise NotImplementedError
        if args.operator == "+":
            return args.operand_1 + args.operand_2
        elif args.operator == "-":
            return args.operand_1 - args.operand_2
        elif args.operator == "*":
            return args.operand_1 * args.operand_2
        elif args.operator == "/":
            return args.operand_1 / args.operand_2
    except ZeroDivisionError:
        raise ZeroDivisionError


def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()
