#!/usr/bin/python3

def validUTF8(data):
    """method to validate UTF8"""
    numbytes = 0

    first_byte = 1 << 7
    second_byte = 1 << 6

    for num in data:
        fb = 1 << 7
        if numbytes == 0:
            while fb & num:
                numbytes += 1
                fb = fb >> 1
            if numbytes == 0:
                continue
            if numbytes == 1 or numbytes > 4:
                return False
        else:
            if not ( & first_byte and not (fb & second_byte)):
                return False
        numbytes -= 1
    return numbytes == 0
