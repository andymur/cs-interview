#!/usr/bin/python3


# 1234
	# 123
		# 12
			# 1
			# 2
		# 23
			#
			# 3
	# 234
		# 34
			# 3 x
			# 4

# 1234 + 123 + 12 + 1 + 2 + 23 + 3 +234 + 34 + 4

# 123
	# 12 (0)
		# 1 (0)
		# 2 (1)
	# 23 (1)
		# 2 (1)
		# 3 (2)

# 123 + 12 + 1 + 2 + 23 + 3

# 121
	# 12
		# 1
		# 2
	# 21
		# 2 x
		# 1
# 121 + 12 + 1 + 2 + 21 + 1

visited = []
calculated = {}

divisor = 10**9 + 7


def substrings(position, word):
	
	#print("working with word: {0} and visited: ".format(word, visited))

	if (position, int(word)) in visited:
		return 0
	else:
		visited.append((position, int(word)))

	if not word:
		return 0
	
	elif len(word) == 1:
		return int(word)

	if int(word) in calculated.keys():
		return calculated[word]
	else:
		result = (int(word) + substrings(position + 1, word[1:]) + substrings(position, word[:-1])) % divisor
		calculated[int(word)] = result
		return result

# 972698438521
# expected 445677619
# actual   445677600
if __name__ == "__main__":
    try:
    	result = substrings(0, very_long_case)
    	visited.sort()
    	print("result is: {0}, substrings: {1}".format(result, visited))
    except:
    	print(calculated)
