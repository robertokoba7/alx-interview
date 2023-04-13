#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """
import sys


def log_parsing(status_code_counts, total_file_size):
    """print log parsing results"""
    total_file_size += file_size
    print("File size: {}".format(total_file_size))
    """print("Total size of file: {}".format(total_file_size))"""
    for key in sorted(status_code_counts.keys()):
        if status_code_counts[key] != 0:
            print("{}: {}".format(key, status_code_counts[key]))


status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0}

total_file_size = 0
line_count = 0
file_size = 0

try:
    # Read input data from stdin
    for line in sys.stdin:
        # Parse input line when matching the expected format
        if line_count != 0 and line_count % 10 == 0:
            log_parsing(status_code_counts, total_file_size)

        elem = line.split(" ")
        line_count += 1

        try:
            file_size += int(elem[-1])
        except BaseException:
            pass

        try:
            status_code = int(elem[-2])
            if status_code in status_code_counts.keys():
                status_code_counts[status_code] += 1
        except IndexError:
            pass
    log_parsing(status_code_counts, total_file_size)

except KeyboardInterrupt:
    log_parsing(status_code_counts, total_file_size)
    raise
