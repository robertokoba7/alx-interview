#!/usr/bin/python3

def validUTF8(data):
    # count tracks how many more continuation bytes are expected
    count = 0
    
    for byte in data:
        if count == 0:
            # Check if the byte is a single byte character (i.e., starts with a 0)
            if (byte >> 7) == 0b0:
                continue
            # Check if the byte starts a multi-byte character
            elif (byte >> 5) == 0b110:
                count = 1
            elif (byte >> 4) == 0b1110:
                count = 2
            elif (byte >> 3) == 0b11110:
                count = 3
            else:
                # Invalid UTF-8 byte sequence
                return False
        else:
            # Check if the byte is a continuation byte (i.e., starts with 10)
            if (byte >> 6) != 0b10:
                return False
            count -= 1
    
    # If there are still expected continuation bytes, it means the data set is incomplete
    return count == 0

