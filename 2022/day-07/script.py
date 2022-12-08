import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], "r")
inputData = inputFile.read().rstrip();

class FSFile:
	def __init__(self, directory, name, size):
		self.directory = directory
		self.name = name
		self.size = size
	# helper to print the file information (@TODO: the indentation of this is a little off)
	def print(self, level=0):
		indent = ("  "*level)
		return indent + "- " + self.name + " (file, size=" + str(self.size) + ")\n"

class FSDirectory:
	def __init__(self, parentDirectory, name):
		self.parentDirectory = parentDirectory
		self.name = name
		self.directories = list()
		self.files = list()
	def addFile(self, file):
		#print("adding file \"" + file.name + "\" into directory \"" + self.name + "\"")
		self.files.append(file)
	def addDirectory(self, directory):
		#print("adding directory \"" + directory.name + "\" into directory \"" + self.name + "\"")
		self.directories.append(directory)
	# helper to get the FSDirectory object within the current directory by name
	def getDirectory(self, directoryName):
		for directory in self.directories:
			if directory.name == directoryName:
				return directory
		raise ValueError("Directory \"" + directoryName + "\" does not exist")
	# helper to print the directory tree (@TODO: the indentation of this is a little off)
	def print(self, level=0):
		indent = ("  "*level)
		output = indent + "- " + self.name + " (dir)\n"
		level += 1
		for directory in self.directories:
			output += directory.print(level)
		for file in self.files:
			output += indent + file.print(level)
		return output
	# returns the full size for the current directory
	def getSize(self):
		size = 0
		for file in self.files:
			size += file.size
		for directory in self.directories:
			size += directory.getSize()
		return size
	# returns the full path for the current directory
	def getPath(self):
		path = list()
		path.append(self.name)
		if (self.parentDirectory != None):
			path.append(self.parentDirectory.getPath()) # recursively append each directory name to the list
		# reverse and join the list with a slash between each directory name,
		# then remove any double slashes (caused by the root being a slash)
		return "/".join(path[::-1]).replace("//", "/")

def buildFS(lines):
	root = FSDirectory(None, "/")
	currentDirectory = root
	for line in lines:
		if (line[0] == "$"): # actual command
			commandLineParts = line.split(" ")[1:] # omit the $ that starts this command
			if (commandLineParts[0] == "cd"): # command starts with cd
				if (commandLineParts[1] == "/"): # change to root directory
					currentDirectory = root
				elif (commandLineParts[1] == ".."): # change to parent directory
					#print("moving from \"" + currentDirectory.name + "\" up to \"" + currentDirectory.parentDirectory.name + "\"")
					currentDirectory = currentDirectory.parentDirectory
				else: # change to named directory
					#print("moving from \"" + currentDirectory.name + "\" down to \"" + commandLineParts[1] + "\"")
					currentDirectory = currentDirectory.getDirectory(commandLineParts[1])
		else: # output of a command
			outputParts = line.split(" ")
			if (outputParts[0] == "dir"): # directory output starts with "dir"
				_,name = outputParts # we only want the name of the directory, not the "dir" that precedes it
				directory = FSDirectory(currentDirectory, name)
				currentDirectory.addDirectory(directory)
			else: # file output
				size,name = outputParts # we want the size and name of the file
				file = FSFile(currentDirectory, name, int(size, 10))
				currentDirectory.addFile(file)
	return root

# gets a dict of all directories with their sizes, keyed by path
def getDirectorySizes(filesystem):
	sizes = {}
	def populateDirectorySizes(directory):
		# use the path as the key b/c the name might not be unique
		path = directory.getPath()
		if path in sizes:
			raise Exception("Path \"" + path + "\" already exists")
		sizes[path] = directory.getSize()
		for d in directory.directories:
			populateDirectorySizes(d)
	populateDirectorySizes(filesystem)
	return sizes;

# gets a dict of all directories with their sizes, keyed by path, that are under the given maximum size
def getDirectoriesUnderSize(filesystem, maximum):
	directorySizes = getDirectorySizes(filesystem)
	#print(directorySizes)
	directories = {}
	for path,size in directorySizes.items():
		if (size <= maximum):
			directories[path] = size
	return directories

# gets the size of all directories (combined) that are under the given maximum size
def getSizeOfDirectoriesUnderSize(filesystem, maximum):
	directories = getDirectoriesUnderSize(filesystem, maximum)
	#print(directories)
	totalSize = 0
	for size in directories.values():
		totalSize += size
	return totalSize

# gets a dict of all directories with their sizes, keyed by path, that are over the given minimum size
def getDirectoriesOverSize(filesystem, minimum):
	directorySizes = getDirectorySizes(filesystem)
	#print(directorySizes)
	directories = {}
	for path,size in directorySizes.items():
		if (size >= minimum):
			directories[path] = size
	return directories

# returns the size of the smallest directory that can be deleted from the given file system (of a given maximum size)
# to leave the amount given as requiredSpace in free/unused space
def getSizeOfDirectoryToDelete(filesystem, maximumSize, requiredSpace):
	sizes = getDirectorySizes(filesystem)
	usedSpace = sizes.get("/")
	freeSpace = maximumSize - usedSpace
	neededSpace = requiredSpace - freeSpace
	#print("-Used space: " + str(usedSpace))
	#print("-Free space: " + str(freeSpace))
	#print("-Needed space: " + str(neededSpace))
	directories = getDirectoriesOverSize(filesystem, neededSpace)
	directorySizes = list(directories.values()) # convert dirt to a list of values so it can be sorted
	directorySizes.sort()
	return directorySizes[0]

filesystem = buildFS(inputData.split("\n"))
#print(filesystem.print())

sizePart1 = getSizeOfDirectoriesUnderSize(filesystem, 100000)
print("Total size of directories under 100000: " + str(sizePart1))

directoriesPart2 = getSizeOfDirectoryToDelete(filesystem, 70000000, 30000000)
print("Size of directory to delete: " + str(directoriesPart2))
