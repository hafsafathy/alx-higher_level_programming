#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""


def print_stats(size, status_code):
    """function

    Args:
        size (int): The accumulated read file size.
        status_code (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(size, status_code)
                c = 1
            else:
                c += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_code)

    except KeyboardInterrupt:
        print_stats(size, status_code)
        raise
