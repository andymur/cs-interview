#!/usr/bin/python3
import sys

if __name__=="__main__":
	# s = sys.argv[1:]
	#s = [-1, 0, 1, 2, -1 ,-4]
	s = [1, 2, 0, -3, 3, -2]
	print("original sequence: ", s)
	for i in range(len(s)):
		for j in range(i+1, len(s)):
			t = (i, j, s[i], s[j], s[i] + s[j])
			print(t)
