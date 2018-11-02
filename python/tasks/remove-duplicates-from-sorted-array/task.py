#!/usr/bin/python3

'''Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. 
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, given input array A = [1,1,2], your function should return length = 2, and A is now [1,2].'''


if __name__ == "__main__":
	a = [1, 1, 1, 1, 2, 2, 3]

	k = 1
	prev = a[0]
	print(a)
	for i in range(len(a)):
		if a[i] != prev:
			a[k] = a[i]
			prev = a[i]
			k += 1
	print(a)
	for i in range(k, len(a)):
		a[i] = 0
	print(a)
