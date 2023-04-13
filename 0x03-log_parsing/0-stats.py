#!/usr/bin/python3
import sys

# metric variables initialized
total_size = 0
status_counts = {}


try:
    # Read input data from stdin
    for i, line in enumerate(sys.stdin):
        # Parse input line when matching the expected format
        try:
            ip_address, _,_,_,status_code, file_size = line.split()
            status_code = int(status_code)
            file_size = int(file_size)
            file_size = int(file_size)
        except ValueError:
            # Skip line if it unmatched the format expected
            continue

        # Print metrics every 10 lines of input
        if i % 10 == 9:
            print("File size:", total_size)
            for code in sorted(status_counts.keys()):
                print(code, ":", status_counts[code])

except KeyboardInterrupt:
    # Print final metric
    print("File size:", total_size)
    for code in sorted(status_counts.keys()):
        print(code, ":", status_counts[code])

