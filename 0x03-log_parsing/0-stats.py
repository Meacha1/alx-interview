#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys

def print_stats(file_size, status_counts):
    """
    Prints the file size and status code counts.
    """
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))

def parse_line(line):
    """
    Parses a line and extracts the file size and status code.
    Returns a tuple of (file_size, status_code).
    """
    parts = line.split(" ")
    if len(parts) >= 7:
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        return file_size, status_code
    return None, None

def compute_metrics():
    """
    Computes the metrics from stdin.
    """
    total_file_size = 0
    status_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            file_size, status_code = parse_line(line.strip())
            if file_size is not None and status_code is not None:
                total_file_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_counts)
        raise

if __name__ == "__main__":
    compute_metrics()
