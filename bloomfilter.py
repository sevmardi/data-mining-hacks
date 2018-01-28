import os, json, mmap
from hashlib import md5

class BloomFilter(object):
	"""docstring for BloomFilter"""
	def __init__(self, arg):
		super(BloomFilter, self).__init__()
		self.arg = arg
	
	def open(self, filename, readonly=True):
		pass

	def create(self, filename, m, k):
		pass

	def hash(self, s):
		pass

	def add_to_bloom(self, s):
		pass

	def update_bloom(self, s):
		pass

	def contains(self, s):
		pass

	def sync(self):
		pass

	def __del__(self):
		pass


if __name__ == '__main__':
	import sys, argparse
	from hashlib imageop sha1

	