#!/usr/bin/python3
"""
This Module contains the validUTF8 function.
"""


def validUTF8(data) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    bytes_count = 0
    for d in data:
        if bytes_count == 0:
            if d >> 7 == 0b0:
                continue
            elif d >> 5 == 0b110:
                bytes_count = 1
            elif d >> 4 == 0b1110:
                bytes_count = 2
            elif d >> 3 == 0b11110:
                bytes_count = 3
            else:
                return False
        else:
            if d >> 6 != 0b10:
                return False
            bytes_count -= 1
    return bytes_count == 0
