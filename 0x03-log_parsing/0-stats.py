#!/usr/bin/python3
"""This module contains a script that reads a stdin line by line
   and computes metrics.
"""

import sys


# Initialize variables to store metrics.
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                      403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_metrics():
    '''prints metrics based o the requrements given in the task'''
    print(f"File size: {total_file_size}")

    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


# This section is to parse the input
try:
    for line in sys.stdin:
        parts = line.split()
        if (len(parts) == 9 and parts[-2].isdigit() and int(parts[-2]) in
                status_code_counts):
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
