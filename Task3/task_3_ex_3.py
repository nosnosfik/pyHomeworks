"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import argparse
import fnmatch
import os
import stat


def get_args():
    """ Parsing data from command line input """
    parser = argparse.ArgumentParser(description='Searches for files by a given pattern')
    parser.add_argument('path', type=str, help='Absolute path for searching')
    parser.add_argument('-p', '--pattern', type=str, help='File match pattern, can consist *, ?')
    return parser.parse_args()


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    found_files = []
    for file in os.listdir(f'{path}'):
        if fnmatch.fnmatch(file, f'{pattern}'):
            found_files.append(f'{os.path.abspath(path)}/{file}')
    return found_files


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    for path in file_paths:
        print(f'{path}', f'{stat.filemode(os.stat(path).st_mode)}')
    print(f'Found {len(file_paths)} file(s).')


def main():
    args = get_args()
    display_result(finder(args.path, args.pattern))


if __name__ == '__main__':
    main()
