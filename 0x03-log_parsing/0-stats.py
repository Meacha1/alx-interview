#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

metrics = {
    'total_size': 0,
    'status_codes': {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    },
    'line_count': 0
}

try:
    for line in sys.stdin:
        parts = line.strip().split(" ")
        if len(parts) == 9:
            ip, _, _, status, size = parts[0], parts[8], parts[7],
            int(parts[6]), int(parts[8])
            if status in metrics['status_codes']:
                metrics['total_size'] += size
                metrics['status_codes'][status] += 1
            metrics['line_count'] += 1
        if metrics['line_count'] % 10 == 0:
            print("File size: {}".format(metrics['total_size']))
            for code, count in sorted(metrics['status_codes'].items()):
                if count > 0:
                    print("{}: {}".format(code, count))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(metrics['total_size']))
    for code, count in sorted(metrics['status_codes'].items()):
        if count > 0:
            print("{}: {}".format(code, count))
