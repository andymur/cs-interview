#!/usr/bin/python3
'''
There is an array of positive integer which represents height of the bloks of the wall.
Compute number of block filled with water

e.g. this wall could be represented by array of height [3, 1, 3]

[]  [] 
[]  []
[][][]
3 1 3

Another example:

                  [][]
                  [][]
      [][]        [][]
      [][]        [][]        [][]
    [][][]  []    [][]    []  [][][]
  [][][][][][][][][][][][][][][][][][]
[][][][][][][][][][][][][][][][][][][]
1 2 3 5 5 2 3 2 2 7 7 2 2 3 2 4 4 3 2

and the answer is 2 cause two blocks will be filled with water in case of eternal rain

'''

def empty_or_not_for_level(original_arr, level):
	return [1 if x >= level else 0 for x in original_arr]

def number_for_line(original_arr, level):
	level_arr = empty_or_not_for_level(original_arr, level)
	lpivot = 0
	rpivot = len(level_arr)

	for i in range(len(level_arr)):
		if level_arr[i] == 1:
			break
		lpivot += 1
	
	for i in reversed(range(len(level_arr))):
		if level_arr[i] == 1:
			break
		rpivot -= 1

	print(level_arr, lpivot, rpivot)
	level_to_count = level_arr[lpivot:rpivot]
	print(level_to_count)
	result = len([x for x in level_to_count if x != 1])
	print("result", result)
	return result

if __name__ == "__main__":
	original_arr = [1,2,3,5,5,2,3,2,2,7,7,2,2,3,2,4,4,3,2]
	s = 0
	for level in range(max(original_arr)):			
		s += number_for_line(original_arr, level + 1)
	print("final result", s)
