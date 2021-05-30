#!/usr/bin/python3


import hashlib
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-md5", required=False, help="hash with md5")
ap.add_argument("-sha1", required=False, help="hash with sha1")
ap.add_argument("-sha224", required=False, help="hash with sha224")
ap.add_argument("-sha256", required=False, help="hash with sha256")
ap.add_argument("-sha384", required=False, help="hash with sha384")
ap.add_argument("-sha512", required=False, help="hash with sha512")

args=vars(ap.parse_args())

def solve(func):
	def wrapper(ps):
		print(func(ps))
	return wrapper	
@solve
def md5(ps):
	mh = hashlib.md5()
	mh.update(ps.encode("utf-8"))
	md5 = mh.hexdigest()
	return md5
@solve
def sha1(ps):
	mh = hashlib.sha1()
	mh.update(ps.encode("utf-8"))
	sha1 = mh.hexdigest()
	return sha1
@solve
def sha224(ps):
	mh = hashlib.sha224()
	mh.update(ps.encode("utf-8"))
	sha224 = mh.hexdigest()
	return sha224
@solve
def sha256(ps):
	mh = hashlib.sha384()
	mh.update(ps.encode("utf-8"))
	sha384 = mh.hexdigest()
	return sha384
@solve
def sha384(ps):
	mh = hashlib.sha384()
	mh.update(ps.encode("utf-8"))
	sha384 = mh.hexdigest()
	return sha384
	
@solve
def sha512(ps):
	mh = hashlib.sha512()
	mh.update(ps.encode("utf-8"))
	sha512 = mh.hexdigest()
	return sha512

def run():
	if len(args) > 0:
		if args["md5"]:
			md5(str(args["md5"]))
		elif args["sha1"]:
			sha1(args["sha1"])
		elif args["sha224"]:
			sha224(args["sha224"])
		elif args["sha256"]:
			sha256(args["sha256"])
		elif args["sha384"]:
			sha384(args["sha384"])
		elif args["sha512"]:
			sha512(args["sha512"])
run()
