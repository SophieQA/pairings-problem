  # Write your solution here!
  # 1. inout: string include unique positive integer
  #   - it won't multiple same integer, they are all  greater than 0
  #   - integer seperated by space
  # 2. output: a set of tuple
  # 3. rule of pairing:
  #   1. 2 elements
  #   2. the first should be smallar than the second
  #   3. all possible pairings of integers
  # 4. if the string only contain one element, return the empty set


def find_pairs(num_string):
	#  1. convert the string to a list of integers
	list_integer = [int(num) for num in num_string.split()]
	pairing_result = set()

	#  2. if the element in the list is smaller than 2, i would return the smpty set
	if len(list_integer) < 2:
		return set()
	
	#  3. Iterate the element in the list to compare with leftover element
	#     - if the element is smaller than the compared one, pairing them as tuple and add to the set
	#     - if the element is greater, ignore it.
	
	for current_one in list_integer:
		for compared_one in list_integer:
			if current_one < compared_one:
				tuple_pair = (current_one, compared_one)
				pairing_result.add(tuple_pair)
				
	#  4. return the set	
	return pairing_result


# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")