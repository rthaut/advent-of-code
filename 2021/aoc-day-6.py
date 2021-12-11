initial_state = "4,2,4,1,5,1,2,2,4,1,1,2,2,2,4,4,1,2,1,1,4,1,2,1,2,2,2,2,5,2,2,3,1,4,4,4,1,2,3,4,4,5,4,3,5,1,2,5,1,1,5,5,1,4,4,5,1,3,1,4,5,5,5,4,1,2,3,4,2,1,2,1,2,2,1,5,5,1,1,1,1,5,2,2,2,4,2,4,2,4,2,1,2,1,2,4,2,4,1,3,5,5,2,4,4,2,2,2,2,3,3,2,1,1,1,1,4,3,2,5,4,3,5,3,1,5,5,2,4,1,1,2,1,3,5,1,5,3,1,3,1,4,5,1,1,3,2,1,1,1,5,2,1,2,4,2,3,3,2,3,5,1,5,1,2,1,5,2,4,1,2,4,4,1,5,1,1,5,2,2,5,5,3,1,2,2,1,1,4,1,5,4,5,5,2,2,1,1,2,5,4,3,2,2,5,4,2,5,4,4,2,3,1,1,1,5,5,4,5,3,2,5,3,4,5,1,4,1,1,3,4,4,1,1,5,1,4,1,2,1,4,1,1,3,1,5,2,5,1,5,2,5,2,5,4,1,1,4,4,2,3,1,5,2,5,1,5,2,1,1,1,2,1,1,1,4,4,5,4,4,1,4,2,2,2,5,3,2,4,4,5,5,1,1,1,1,3,1,2,1"

# initial_state = "3,4,3,1,2" # test data

def simulate_basic(days):
	# print("Initial state: " + initial_state)
	values = [int(x) for x in initial_state.split(",")]
	day = 0
	while day < days:
		new = []
		for idx, val in enumerate(values):
			val -= 1
			if val < 0:
				# reset the count and add a new one at day 8
				val = 6
				new.append(8)
			values[idx] = val
		day += 1
		values += new # append new items to existing items
		# print(f"After {str(day):>2} days: " + ",".join([str(x) for x in values]))
	print("Count after " + str(day) +" days: " + str(len(values)))

# this uses a dictionary, where each day in the cycle is a key
# then we just track the number of fish on each day,
# and move them through the dictionary to simulate the days passing
def simulate_alternate(days):
	values = {
		"0": 0,
		"1": 0,
		"2": 0,
		"3": 0,
		"4": 0,
		"5": 0,
		"6": 0,
		"7": 0,
		"8": 0,
	}
	for value in initial_state.split(","):
		values[value] += 1
	day = 0
	while day < days:
		tmp_values = {}
		# first decrement all days by copying their count into a temporary dictionary
		for value in values:
			tmp_value = str(int(value) - 1)
			tmp_values[tmp_value] = values[value]

		tmp_values["8"] = tmp_values["-1"] # -1 is when we "spawn", so copy the count into day 8
		tmp_values["6"] += tmp_values["-1"] # -1 is when we reset too, so add the count into day 6
		del tmp_values["-1"] # remove -1 now
		values = tmp_values.copy() # replace the values with the temporary dictionary
		day += 1
	count = 0
	for value in values:
		count += values[value]
	print("Count after " + str(day) +" days: " + str(count))

simulate_basic(18)
simulate_basic(80)
print()

simulate_alternate(18)
simulate_alternate(80)
simulate_alternate(256)
