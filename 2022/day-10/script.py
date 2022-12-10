import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], "r")
inputData = inputFile.read().rstrip();

instructions = inputData.split("\n")

# gets the signal strengths for the given instructions at the specified cycles
def getSignalStrengths(instructions, targetCycles = []):
	strengths = {} # keys are cycles, values are signal strengths

	# register starts at 1
	register = 1

	cycleCount = 0
	def tick():
		nonlocal cycleCount # use variable from parent scope
		cycleCount += 1
		if cycleCount in targetCycles:
			strengths[cycleCount] = cycleCount * register

	for instruction in instructions:
		tick() # always tick BEFORE processing instruction
		inst = instruction[0:4] # first 4 characters of instruction
		if (inst == "addx"): # only other instruction is noop, which doesn't do anything
			tick() # addx requires 2 ticks, so we tick before incrementing the register
			_,value = instruction.split(" ")
			register += int(value, 10)

	return strengths

# gets the pixels for the given instructions, using a grid of specified row and col sizes
def getPixels(instructions, rows, cols):
	# make a grid of empty pixels to start with
	pixels = [[" " for i in range(cols)] for j in range(rows)]

	register = 1
	sprites = [register - 1, register, register + 1]
	pixelCol = 0
	pixelRow = 0

	cycleCount = 0
	def tick():
		nonlocal pixels, pixelCol, pixelRow, cycleCount # use variables from parent scope

		# check pixel against sprite BEFORE moving the pixel and incrementing the cycle
		if pixelCol in sprites: # we only render a pixel if it falls on the active sprite pixels
			pixels[pixelRow][pixelCol] = "#"

		cycleCount += 1
		pixelCol += 1

		# when we reach the end of the row, reset the column position and move into the next row
		if cycleCount % cols == 0:
			pixelCol = 0
			pixelRow += 1

	for instruction in instructions:
		tick() # always tick BEFORE processing instruction
		inst = instruction[0:4] # first 4 characters of instruction
		if (inst == "addx"): # only other instruction is noop, which doesn't do anything
			tick() # addx requires 2 ticks, so we tick before incrementing the register
			_,value = instruction.split(" ")
			register += int(value, 10)
			sprites = [register - 1, register, register + 1] # sprites are the 3 pixels centered on the register position

	return pixels

# renders the pixels, which are in an array of arrays, into a nice grid
def renderPixels(pixels):
	print()
	for row in pixels:
		for pixel in row:
			print(pixel, end="")
		print()
	print()

strengths = getSignalStrengths(instructions, [20,60,100,140,180,220])
print("Sum of signal strengths: " + str(sum(strengths.values()))) # sum up the values of the map of strengths

pixels = getPixels(instructions, 6, 40)
renderPixels(pixels)
