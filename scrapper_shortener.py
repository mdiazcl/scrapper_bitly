from tiny_reverser import *
from hash_maker import *
import random

try:
	hash_count = 10 # Set this number
	for x in range(hash_count):
		hashurl = hash_maker(hash_min=4, hash_max=7)
		url_bitly = "http://bit.ly/" + hashurl
		url_reverse = reverse_bitly(url_bitly)
	
		if url_reverse is not None:
			print "{0} -> {1}".format(url_bitly, url_reverse)
except Exception, e:
	exit()
