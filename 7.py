#!/usr/bin/env python
import binascii
import os

import png


DATA_FILE = 'oxygen.png'
DATA_DIR = 'data'


def main():

    print "-" * 80
    root_dir = os.path.dirname(__file__)
    image_filepath = os.path.abspath(
        os.path.join(root_dir, DATA_DIR, DATA_FILE))
    print "opening=%s" % image_filepath
    print "-" * 80

    image_file = png.Reader(filename=image_filepath)
    width, height, pixels, metadata = image_file.read()
    print "width=%s" % width
    print "height=%s" % height
    print "-" * 80
    for key in metadata:
        print '%s=%s' % (key, metadata[key])
    print "-" * 80

    rows = list(pixels)
    print "row_length=%s" % len(rows)

    i = 0
    for row in rows:
        if row[0] == row[1] and row[1] == row[2]:
            codes = [unichr(item) for item in row]
            message = ''.join([unichr(item) for item in row])
            print i, message
            separator = max(codes)
            letters = message.split(separator)
            answer = ''
            for letter in letters:
                answer = answer + letter
            print answer

            initial_char = ''
            readable_answer = ''
            for char in answer:
                if char != initial_char:
                    readable_answer = readable_answer + char
                    initial_char = char
            print readable_answer

        print "-" * 80
        i += 1

    for value in [105, 10, 16, 101, 103, 14, 105, 16, 121]:
        print [unichr(value)]

if __name__ == '__main__':
    main()