#!/usr/bin/env python3

from sys import argv
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from argparse import ArgumentParser

hash_types = {"-md5":md5, "-sha1":sha1, "-sha224":sha224,\
"-sha256":sha256, "-sha384":sha384, "-sha512":sha512}

ap=ArgumentParser()
for key in hash_types:
    ap.add_argument(key, required=False, help=f"{key} hash algorithm")
args=vars(ap.parse_args())

def phash(input_text, htype):
    """This function takes the `htype` hash algorithm on the input_text\
    and prints it as output to stdout"""

    hash_maker = htype()
    hash_maker.update(input_text.encode("utf-8"))
    output = hash_maker.hexdigest()
    print(output)

def main():
    """This is the main function, and checks the user inputs and then calls the phash function"""

    if len(argv) > 1:
        uhtype = argv[1].lstrip("-")
        if input_text:=args[uhtype]:
            phash(input_text, hash_types[argv[1]])
    else:
        ap.print_help()

if __name__ == "__main__":
    main()
