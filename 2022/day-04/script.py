import sys

# read input data from file specified as first command line argument
input_file = open(sys.argv[1], 'r')
input_data = input_file.read().rstrip();

# make an array of pairs
pairs = [pair.split(",") for pair in input_data.split("\n")]
#print(pairs)

fully_covered = 0
partially_covered = 0
for pair in pairs:
	range1 = [int(assignment, 10) for assignment in pair[0].split("-")]
	range2 = [int(assignment, 10) for assignment in pair[1].split("-")]

	# verbose variable names to make the conditions below easier to understand
	range1_start,range1_end = range1
	range2_start,range2_end = range2

	# fully covered ranges: compare outer bounds
	if (range1_start <= range2_start and range2_end <= range1_end):
		# first assignment fully covers second assignment
		fully_covered += 1
		partially_covered += 1
	elif (range2_start <= range1_start and range1_end <= range2_end):
		# second assignment fully covers first assignment 
		fully_covered += 1
		partially_covered += 1

	# partially covered ranges: check if one outer bound is within the other range
	elif (range1_start <= range2_start and range2_start <= range1_end):
		# start of second assignment is within first assignment
		partially_covered += 1
	elif (range2_start <= range1_start and range1_start <= range2_end):
		# start of first assignment is within second assignment
		partially_covered += 1
	elif (range1_start <= range2_end and range2_end <= range1_end):
		# end of second assignment is within first assignment
		partially_covered += 1
	elif (range2_start <= range1_end and range1_end <= range2_end):
		# end of first assignment is within second assignment
		partially_covered += 1

print("Fully covered ranges: ", str(fully_covered))
print("Partially covered ranges: ", str(partially_covered))
