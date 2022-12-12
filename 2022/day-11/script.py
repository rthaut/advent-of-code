import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], "r")
inputData = inputFile.read().rstrip();

monkeys = list()

class Monkey:
	def __init__(self, items, operation, testDenominator, passTarget, failTarget):
		self.items = items
		self.operation = operation
		self.testDenominator = testDenominator
		self.passTarget = passTarget
		self.failTarget = failTarget
		self.inspectionCount = 0
	def __str__(self): # override the print() to output like the input
		output = ""
		output += "  Starting items: " + ", ".join([str(item) for item in self.items]) + "\n"
		output += "  Operation: new = " + self.operation + "\n"
		output += "  Test: divisible by " + str(self.testDenominator) + "\n"
		output += "    If true: throw to monkey " + str(self.passTarget) + "\n"
		output += "    If false: throw to monkey " + str(self.failTarget) + "\n"
		return output
	def inspect(self):
		while len(self.items) > 0:
			item = self.items.pop() # get the first item and clear it from the list
			item = self.performOperation(item)
			item = item // 3 # divide by 3 and round down (floor)
			to = self.passTarget if self.performTest(item) else self.failTarget
			self.throw(item, to)
			self.inspectionCount += 1
	def throw(self, item, to):
		monkeys[to].catch(item)
	def catch(self, item):
		self.items.append(item)
	def performOperation(self, item):
		# convert the string describing the operation into something that can be performed mathematically
		first,operation,second = self.operation.split(" ")
		first = item if first == "old" else int(first, 10)
		second = item if second == "old" else int(second, 10)
		if operation == "*":
			return first * second
		elif operation == "+":
			return first + second
	def performTest(self, item):
		return item % self.testDenominator == 0 # return true if the item can be evenly divided by the denominator

# initialize all monkeys into the global list from the input data
def initMonkeys(notes):
	monkeys.clear() # clear the list of monkeys between runs
	for note in notes:
		# parse the text of each monkey in the input
		noteLines = note.split("\n")
		items = [int(item, 10) for item in noteLines[1].replace("  Starting items: ", "").split(", ")]
		operation = noteLines[2].replace("  Operation: new = ", "")
		testDenominator = int(noteLines[3].replace("  Test: divisible by ", ""), 10)
		passTarget = int(noteLines[4].replace("    If true: throw to monkey ", ""), 10)
		failTarget = int(noteLines[5].replace("    If false: throw to monkey ", ""), 10)
		monkeys.append(Monkey(items, operation, testDenominator, passTarget, failTarget))

def playRound(monkeys):
	for monkey in monkeys:
		monkey.inspect()

def printMonkeyItems(monkeys):
	for i,monkey in enumerate(monkeys):
		print("Monkey " + str(i) + ": " + ", ".join([str(item) for item in monkey.items]))

def getMonkeyBusiness(monkeys):
	counts = list()
	for monkey in monkeys:
		counts.append(monkey.inspectionCount)
	sortedCounts = sorted(counts)[::-1] # sort the counts in descending order (most to least)
	return sortedCounts[0] * sortedCounts[1] # multiply the top 2 values

def play(rounds):
	initMonkeys(inputData.split("\n\n"))
	#for i,monkey in enumerate(monkeys):
		#output = "Monkey " + str(i) + ":\n"
		#print(monkey)

	for i in range(rounds):
		playRound(monkeys)
		#print("After round " + str(i+1) + ", the monkeys are holding items with these worry levels:")
		#printMonkeyItems(monkeys)

play(20)
print("Level of monkey business after 20 rounds: " + str(getMonkeyBusiness(monkeys)))
