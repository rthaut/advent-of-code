import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], 'r')
inputData = inputFile.read().rstrip();

# make an array of arrays for each elf with calorie counts as integers
data = [[int(calories, 10) for calories in group.split("\n")] for group in inputData.split("\n\n")]
#print(data)

# make an array of total calorie counts
counts = []
for elf in data:
	counts.append(sum(elf))
#print(counts)

# sort the counts in ascending order (lowest to highest)
counts.sort()

print("Highest calorie count: " + str(counts[-1])) # elf with the most calories is the last one
print("Calorie count across top 3 elves: " + str(sum(counts[-3:]))) # sum of top 3 elves
