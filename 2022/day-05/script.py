import sys

# read input data from file specified as first command line argument
input_file = open(sys.argv[1], 'r')
input_data = input_file.read().rstrip();

drawing,procedure = input_data.split("\n\n")
#print(drawing)
#print(procedure)

def read_drawing_line(line):
	data = []
	i = 0
	while i < len(line):
		data.append(line[i+1:i+2])
		i += 4
	return data

def build_stacks(drawing):
	lines = drawing.split("\n")[::-1]
	key = read_drawing_line(lines.pop(0))
	stacks = [[] for stack in range(len(key))] # list of lists to act as stacks
	for line in lines:
		crates = read_drawing_line(line)
		for idx,crate in enumerate(crates):
			if (crate != ' '):
				stacks[idx].append(crate)
	#print(stacks)
	return stacks

# move crates from one stack to another individually
def perform_procedure1(procedure, stacks):
	for instruction in procedure.split("\n"):
		_,count,_,origination,_,destination = instruction.split(" ")
		for i in range(int(count, 10)):
			crate = stacks[int(origination, 10)-1].pop() # take the top crate from the origination stack
			stacks[int(destination, 10)-1].append(crate) # put the pop'd crate on the destination stack

# move crates from one stack to another in batches
def perform_procedure2(procedure, stacks):
	for instruction in procedure.split("\n"):
		_,count,_,origination,_,destination = instruction.split(" ")
		crates = list() # temporary list to hold all crates pop'd this operation
		for i in range(int(count, 10)):
			crate = stacks[int(origination, 10)-1].pop() # pop the top crate(s) into the temp list
			crates.append(crate)
		stacks[int(destination, 10)-1] += crates[::-1] # reverse pop'd crates and concatenate to stack

def get_stack_message1():
	stacks = build_stacks(drawing);
	#print(stacks)
	perform_procedure1(procedure, stacks)
	return get_stack_message(stacks)

def get_stack_message2():
	stacks = build_stacks(drawing);
	#print(stacks)
	perform_procedure2(procedure, stacks)
	return get_stack_message(stacks)

def get_stack_message(stacks):
	top_crates = list()
	for stack in stacks:
		top_crates.append(stack[-1])
	return ''.join(top_crates)

print("Top crates (style 1): " + get_stack_message1())
print("Top crates (style 2): " + get_stack_message2())

