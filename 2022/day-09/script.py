import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], "r")
inputData = inputFile.read().rstrip();

commands = [command.split(" ") for command in inputData.split("\n")]

class Knot:
	def __init__(self):
		self.y = 0
		self.x = 0
		self.visited = [tuple([0,0])] # initial position is considered visited
	def move(self, directions, amount = 1):
		for direction in list(directions):
			if direction == "U":
				self.y += amount
			elif direction == "D":
				self.y -= amount
			elif direction == "R":
				self.x += amount
			elif direction == "L":
				self.x -= amount
		self.visited.append(tuple([self.y, self.x]))
	def printVisitedGrid(self): # prints a 2-D grid of visited positions
		#print(set(self.visited))
		# positions can be negative, so we need to know the min and max of each axis
		maxY = 0
		maxX = 0
		minY = 0
		minX = 0
		for coords in set(self.visited): # visited is a list, convert to a set to get unique positions
			y,x = coords
			if (y > maxY): maxY = y
			elif (y < minY): minY = y
			if (x > maxX): maxX = x
			elif (x < minX): minX = x
		# this will give is the total amount between min and max on each axis
		rows = abs((minY * -1) + maxY)
		cols = abs((minX * -1) + maxX)
		#print("Grid size: " + str(rows) + "x" + str(cols))
		grid = [[" " for x in range(cols + 1)] for y in range(rows + 1)]
		for coords in set(self.visited): # visited is a list, convert to a set to get unique positions
			y,x = coords
			 # offset the coordinates by the smallest negative value per axis,
			 # which is like drawing from the midpoint
			grid[abs(minY) + y][abs(minX) + x] = "#"
		for row in grid[::-1]: # reverse the rows, because we are graphing from bottom to top
			for position in row:
				print(position, end="")
			print()
		print()


class Head(Knot):
	def __init__(self):
		super().__init__() # initialize the Knot that Head extends
		self.tail = Knot()
	def move(self, directions, amount = 1):
		#print("Moving Head " + directions)
		super().move(directions, amount) # move the Head
		# everything else is logic for moving the Tail to stay in touch with the Head
		directions = "" # reset directions for moving the Tail
		yDistance = self.y - self.tail.y
		xDistance = self.x - self.tail.x
		if (yDistance > 1): # Head is 2 or more positions above Tail
			directions += "U" # move Tail up for sure, as it isn't currently touching Head on Y axis
			if (xDistance > 0): # Head is also 1 or more positions to the right of Tail
				directions += "R" # also move Tail to the right (effectively a diagonal move)
			elif (xDistance < 0): # Head is also 1 or more positions to the left of Tail
				directions += "L" # also move Tail to the left (effectively a diagonal move)
		elif (yDistance < -1): # Head is 2 or more positions below Tail
			directions += "D" # move Tail down for sure, as it isn't currently touching Head on Y axis
			if (xDistance > 0): # Head is also 1 or more positions to the right of Tail
				directions += "R" # also move Tail to the right (effectively a diagonal move)
			elif (xDistance < 0): # Head is also 1 or more positions to the left of Tail
				directions += "L" # also move Tail to the left (effectively a diagonal move)
		if (xDistance > 1): # Head is 2 or more positions to the right Tail
			directions += "R" # move Tail right for sure, as it isn't currently touching Head on X axis
			if (yDistance > 0): # Head is also 1 or more positions above Tail
				directions += "U" # also move Tail up (effectively a diagonal move)
			elif (yDistance < 0): # Head is also 1 or more positions below Tail
				directions += "D" # also move Tail down (effectively a diagonal move)
		elif (xDistance < -1): # Head is 2 or more positions to the left Tail
			directions += "L" # move Tail left for sure, as it isn't currently touching Head on X axis
			if (yDistance > 0): # Head is also 1 or more positions above Tail
				directions += "U" # also move Tail up (effectively a diagonal move)
			elif (yDistance < 0): # Head is also 1 or more positions below Tail
				directions += "D" # also move Tail down (effectively a diagonal move)
		if len(directions) > 0: # only move the Tail when needed
			#print("Moving Tail " + directions)
			self.tail.move(directions, amount)

def simulate(commands):
	head = Head()
	for command in commands:
		direction,amount = command
		amount = int(amount, 10)
		for r in range(amount):
			head.move(direction, 1)
			#print() # empty line for separating movements
	#head.tail.printVisitedGrid()
	print("Positions visited by Tail at least once: " + str(len(set(head.tail.visited)))) 

simulate(commands)
