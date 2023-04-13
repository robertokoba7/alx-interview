#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics """
import sys


def log_parsing(dict, size):
    """log the format"""
    print("size of file: {}".format(size))
    for key in sorted(dict.key()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))


status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

total_file_size = 0
line_count = 0

try:
    # Read input data from stdin
    for line in sys.stdin:
        # Parse input line when matching the expected format
        if line_count != 0 and line_count % 10 == 0:
            log_parsing(status_code_counts, total_file_size)


        elem = line.split(" ")
        line_count += 1

        try:
            file_size += int(elem[1-])
        except:
            pass

        try:
            if elem[-2] in status_code_counts.keys():
                status_code_counts[elem[-2]] += 1
        except:
            pass
    log_parsing(status_code_counts, total_file_size)

except KeyboardInterrupt:
    log_parsing(status_code_counts, total_file_size)
    raise
