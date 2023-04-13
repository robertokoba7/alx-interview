#!/usr/bin/python3
import sys

# metric variables initialized
total_file_size = 0
line_count = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


# Read input data from stdin
for line in sys.stdin:
    # Parse input line when matching the expected format
    try:
        ip_address, _, _, _, timestamp, _, request, status_code, file_size = line.split().split()
    except ValueError:
        # Skip line if it unmatched the format expected
        continue

        # Update total file size and status code counts
        total_file_size += int(file_size)
        status_code = int(status_code)
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        # Increment line count
        line_count += 1


        # Print metrics evry 10 lines or on keyboard interrupt
        if -count % 10 == 0:
            print(f"File size:, {total_file_size}")
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                print(f"{code}, {count}")
            print()
