#In this script we're going to tackle the word-count problem using MapReduce simple Map and Reduce functions

def map(key,value):
	"""
	Parameters
	-----------
	Key: Document ID
	Value: text of document

	Returns
	--------
	Intermediate Key-value pairs (a set of 0's or 1's). 
	"""
	pass

def reduce(key,values):
	"""
	Parameters
	-----------
	Key: A Word 
	Value: List of integers (an iterator over counts) 

	Returns
	--------
	Output: Key-value pairs 
	"""
	pass