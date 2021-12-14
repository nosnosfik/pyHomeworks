"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""
import math
import operator
import argparse


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='Perform mathematical, logical and comparison operations')
    parser.add_argument('data', nargs='*', help='Data for calculations')
    return parser.parse_args()


global result


def calculate(args):
    """ Calculating expression with data from get_args() function """
    args = get_args()
    exec_string = ""
    exec_method = None
    for arg in args.__dict__:  # getting values from CLI and collecting them to string that will be executed
        for index, value in enumerate(args.__dict__[arg]):
            if not index:
                exec_string += f'{value}('
                exec_method = value
            else:
                if value.isnumeric():
                    exec_string += f'{value},'
                else:
                    raise TypeError
        exec_string = exec_string[:-1] + ')'  # Trimming last comma and making complete expression
    try:
        if exec_method in operator.__all__:
            exec(f'global result; result = operator.{exec_string}')
            return result
        elif exec_method in math.__dict__.keys():
            exec(f'global result; result = math.{exec_string}')
            return result
        else:
            raise NotImplementedError
    except ZeroDivisionError:
        raise ZeroDivisionError


def main():
    args = None
    print(calculate(args))


if __name__ == '__main__':
    main()
