import sys
import string

numberWords = ["one","two","three","four","five","six","seven","eight","nine"]

def getInputData():
	# read input data from file specified as first command line argument
	return open(sys.argv[1], "r").read().rstrip();

def getCalibartionValues1(lines):
	numbers = [[] for i in range(len(lines))]
	for i,line in enumerate(lines):
		# gets an array of all characters that are digits
		numbers[i] = [int(char) for char in list(line) if char.isdigit()]
	# print(str(numbers))
	values = []
	for i in range(len(lines)):
		values.append((numbers[i][0]*10) + numbers[i][-1])
	# print("Calibration 1 values: " + str(values))
	return values

def getCalibartionValues2(lines):
	numbers = [[] for i in range(len(lines))]
	for i,line in enumerate(lines):
		pos = 0
		while pos < len(line):
			substr = line[pos:]
			for x,word in enumerate(numberWords):
				# print("Checking for word \"" + word + "\" in substring: " + substr)
				if substr.startswith(word):
					# print("> Found word \"" + word + "\" in substring: " + substr)
					numbers[i].append(x+1)
					break
			# print("Finished checking for words, now checking next char for digit: " + line[pos:])
			if pos < len(line) and line[pos].isdigit():
				numbers[i].append(int(line[pos]))
			pos += 1
		# print()
	# print(str(numbers))
	values = []
	for i in range(len(lines)):
		values.append((numbers[i][0] * 10) + numbers[i][-1])
	# print("Calibration 2 values: " + str(values))
	return values

def main():
	inputData = getInputData()
	lines = inputData.splitlines()
	values1 = getCalibartionValues1(lines)
	print("Sum of initial calibration values: " + str(sum(values1)))
	values2 = getCalibartionValues2(lines)
	print("Sum of alternate calibration values: " + str(sum(values2)))


main()
