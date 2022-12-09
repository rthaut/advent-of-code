import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], "r")
inputData = inputFile.read().rstrip();

# split input data into array of arrays (matrix) and convert all values to integers
forest = [[int(tree, 10) for tree in list(row)] for row in inputData.split("\n")]

def isTreeVisible(rowIdx, colIdx, forest):
	above = True
	below = True
	left = True
	right = True

	height = forest[rowIdx][colIdx]
	rowCount = len(forest)
	colCount = len(forest[0])

	if rowIdx > 0: # check above
		for i in reversed(range(0, rowIdx)):
			# move up starting from one tree above (so iterating down across rows in the same column)
			if forest[i][colIdx] >= height:
				above = False
				break

	if rowIdx < rowCount: # check below
		for i in range(rowIdx + 1, rowCount):
			# move down starting from one tree below (so iterating up across rows in the same column)
			if forest[i][colIdx] >= height:
				below = False
				break

	if colIdx > 0: # check left
		for i in reversed(range(0, colIdx)):
			# move left starting from one tree before (so iterating down across columns in the same row)
			if forest[rowIdx][i] >= height:
				left = False
				break

	if colIdx < colCount: # check right
		for i in range(colIdx + 1, colCount):
			# move down starting from one tree below (so iterating up across columns in the same row))
			if forest[rowIdx][i] >= height:
				right = False
				break

	#print("Above: "+str(above)+", Left: "+str(left)+", Below: "+str(below)+", Right: "+str(right))
	return above,left,below,right

def getTreeScenicScore(rowIdx, colIdx, forest):
	above = 0
	below = 0
	left = 0
	right = 0

	height = forest[rowIdx][colIdx]
	rowCount = len(forest)
	colCount = len(forest[0])

	if rowIdx > 0: # check above
		for i in reversed(range(0, rowIdx)):
			# move up starting from one tree above (so iterating down across rows in the same column)
			above += 1
			if forest[i][colIdx] >= height:
				break

	if rowIdx < rowCount: # check below
		for i in range(rowIdx + 1, rowCount):
			# move down starting from one tree below (so iterating up across rows in the same column)
			below += 1
			if forest[i][colIdx] >= height:
				break

	if colIdx > 0: # check left
		for i in reversed(range(0, colIdx)):
			# move left starting from one tree before (so iterating down across columns in the same row)
			left += 1
			if forest[rowIdx][i] >= height:
				break

	if colIdx < colCount: # check right
		for i in range(colIdx + 1, colCount):
			# move down starting from one tree below (so iterating up across columns in the same row))
			right += 1
			if forest[rowIdx][i] >= height:
				break

	#print("Above: "+str(above)+", Left: "+str(left)+", Below: "+str(below)+", Right: "+str(right))
	return above*left*below*right

def getVisibleTrees(forest):
	visibleTrees = list()
	for rowIdx,row in enumerate(forest):
		for colIdx,col in enumerate(row):
			above,left,below,right = isTreeVisible(rowIdx, colIdx, forest)
			if above or below or left or right:
				visibleTrees.append([rowIdx, colIdx])
	return visibleTrees

def getTreeScenicScores(visibleTrees, forest):
	scores = list()
	for tree in visibleTrees:
		scores.append(getTreeScenicScore(tree[0], tree[1], forest))
	return scores

visibleTrees = getVisibleTrees(forest)
print("Visible tree count: " + str(len(visibleTrees)))

scores = getTreeScenicScores(visibleTrees, forest)
#print("Visible tree scenic scores:")
#print(scores)
print("Highest scenic score: " + str(sorted(scores)[-1]))
