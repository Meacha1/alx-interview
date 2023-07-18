#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

total_file_size = 0
status_codes = {}

try:
    for count, line in enumerate(sys.stdin, 1):
        line = line.strip()
        data = line.split()
        if len(data) >= 7:
            file_size = int(data[-1])
            status_code = data[-2]

            total_file_size += file_size

            if status_code.isdigit():
                status_code = int(status_code)
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1

        if count % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_codes.keys()):
                print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))
