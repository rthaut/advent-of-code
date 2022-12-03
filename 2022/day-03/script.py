import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], 'r')
inputData = inputFile.read().rstrip();

# make an array of rucksacks
rucksacks = inputData.split("\n")

priorities = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# splits an string into `count` arrays of strings
def split_string(arr, count):
	half = len(arr) // count
	return [arr[:half], arr[half:]]

# returns an array of arrays, where each inner array has `size` items from the original array
# similar to `chunk` from other languages
def group_array(arr, size):
	groups = []
	for x in range(0, len(rucksacks), size):
		groups.append(rucksacks[x:x+size])
	return groups

sum_part1 = 0
for rucksack in rucksacks:
	compartments = split_string(rucksack, 2) # split each rucksack into 2 compartments
	same = [i for i in compartments[0] if i in compartments[1]][0] # get first item that is in both compartments
	sum_part1 += priorities.index(same) + 1 # get the 0-based index of the priority, then add 1 for the offset (a = 1)

sum_part2 = 0
for group in group_array(rucksacks, 3): # split rucksack arrays into groups of 3
	same = [i for i in group[0] if i in group[1] and i in group[2]][0] # get first item that is in all 3 groups
	sum_part2 += priorities.index(same) + 1 # get the 0-based index of the priority, then add 1 for the offset (a = 1)

print("Sum of priorities for part 1: " + str(sum_part1))
print("Sum of priorities for part 2: " + str(sum_part2))
