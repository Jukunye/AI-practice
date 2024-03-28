#!/usr/bin/python3
"""
A simple script to parse input lines and count status codes.
"""
import sys


if __name__ == '__main__':
    stat = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0
    total_size = 0

    def print_stat() -> None:
        """Prints the total file size and the count of each status code."""
        print("File size: {:d}".format(total_size))
        for key, value in sorted(stat.items()):
            if value:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                status_code = int(parts[-2])
                total_size += int(parts[-1])
                if status_code in stat:
                    stat[status_code] += 1
            except BaseException:
                pass
            if line_count % 10 == 0:
                print_stat()
        print_stat()
    except KeyboardInterrupt:
        print_stat()
        raise
