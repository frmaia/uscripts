#!/usr/bin/python

import sys
from string import join
import string
from optparse import OptionParser
import random


def main(args):
	parser = OptionParser(description="Print a hexadecimal string.")
	parser.usage="%prog [options]"
	parser.add_option('-s', '--size', dest='str_size', default=32, help="string size ( Default: 32 )")

	options, parsed_args = parser.parse_args(args)

	print ''.join(random.choice(string.hexdigits) for n in xrange(int(options.str_size))).lower()


if __name__ == "__main__":
	main(sys.argv[1:])

	
