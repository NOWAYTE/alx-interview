#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Returns True if data is a valid UTF-8 encoding else return False
    :param data:
    :return:
    """
    r_bytes = 0

    for i in data:
        byte = i & 0xFF

        if r_bytes == 0:
            mask = 1 << 7
            while byte & mask:
                r_bytes += 1
                mask >>= 1

            if r_bytes == 0:
                continue

            if r_bytes == 1 or r_bytes > 4:
                return False

            r_bytes -= 1
        else:
            if byte >> 6 != 0b10:
                return False
            r_bytes -= 1

    return r_bytes == 0
