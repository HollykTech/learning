#!/bin/python3
import sys, os
allarg=sys.argv
lang=sys.argv[1]
ext=sys.argv[2]
if '-h' in allarg:
	print("Try: learning.py <language> <extension arq>")
else:
	try:
		os.system('mkdir ~/learning/'+lang)
		os.system('touch ~/learning/'+lang+'/map.'+ext)
	except:
		print("Error: use -h to help")
