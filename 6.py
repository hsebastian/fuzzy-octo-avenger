#!/usr/bin/env python
"""
Hints:
amazing. zoom in
zoom in
[:3] todo: tell everyone that [:n] is to take the first n characters...
yes. find the zip.
welcome to my zipped list.
hint1: start from 90052
hint2: answer is inside the zip
it's in the air. look at the letters. 
"""
import os
import re
import zipfile


DATA_FILE = 'channel.zip'
DATA_DIR = 'data'
FILE_EXTENSION = 'txt'


def main():
    root_dir = os.path.dirname(__file__)
    zip_filepath = os.path.abspath(
        os.path.join(root_dir, DATA_DIR, DATA_FILE))
    print "Opening: ", zip_filepath

    with zipfile.ZipFile(zip_filepath, 'r') as myzip:
        nothing = str(90052)
        comments = ''
        while nothing is not None:
            member_name = '.'.join([nothing, FILE_EXTENSION])
            print zip_filepath, member_name
            with myzip.open(member_name) as myfile:
                text = myfile.read()
                print text
                match = re.search("Next nothing is (\d+)", text)
                if match is None:
                    print "Reached the end"
                    break
                nothing = match.group(1)

            zip_info = myzip.getinfo(member_name)
            comments = comments + zip_info.comment
        print comments


if __name__ == '__main__':
    main()
