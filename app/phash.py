#!/usr/bin/env python3

from sys import argv
from os import path
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from argparse import ArgumentParser

hash_types = {"-md5":md5, "-sha1":sha1, "-sha224":sha224,\
"-sha256":sha256, "-sha384":sha384, "-sha512":sha512}

ap=ArgumentParser()
for key in hash_types:
    ap.add_argument(key, required=False, help=f"{key} hash algorithm")
args=vars(ap.parse_args())

def phash(user_input, htype):
    """This function takes the `htype` hash algorithm on the `user_input`\
    and prints it as output to stdout"""

    #to hsahing the file, reads the user_input's data if it was a file, then hashes the data
    if path.exists(user_input):
        with open(user_input, "rb") as input_file:
            data = input_file.read()
    else:
        data = user_input

    hash_maker = htype()
    hash_maker.update(data)
    output = hash_maker.hexdigest()
    print(output)

def main():
    """This is the main function, and checks the user inputs and then calls the phash function"""

    if len(argv) > 1:
        uhtype = argv[1].lstrip("-")
        if user_input:=args[uhtype]:
            phash(user_input, hash_types[argv[1]])
    else:
        ap.print_help()

if __name__ == "__main__":
    main()
