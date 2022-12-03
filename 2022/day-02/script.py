import sys

# read input data from file specified as first command line argument
inputFile = open(sys.argv[1], 'r')
inputData = inputFile.read().rstrip();

# make an array of arrays for each round
rounds = [round.split(" ") for round in inputData.split("\n")]
#print(rounds)

# return points based on win (6), draw (3), or loss (0)
def play_style1(opponent_move, player_move):
	if (opponent_move == player_move):
		return 3 # draw
	elif (player_move == 'rock' and opponent_move == 'scissors'):
		return 6 # win: paper beats rock
	elif (player_move == 'paper' and opponent_move == 'rock'):
		return 6 # win: paper beats rock
	elif (player_move == 'scissors' and opponent_move == 'paper'):
		return 6 # win: scissors beats rock
	elif (opponent_move == 'rock' and player_move == 'scissors'):
		return 0 # loss: rock beats scissors
	elif (opponent_move == 'paper' and player_move == 'rock'):
		return 0 # loss: paper beats rock
	elif (opponent_move == 'scissors' and player_move == 'paper'):
		return 0 # loss: scissors beats rock
	raise ValueError("Undefined outcome for " + opponent_move + " vs. " + player_move)

# return player's move based on needing to win (6), draw (3), or lose (0)
def play_style2(opponent_move, needed_outcome):
	if (needed_outcome == 3):
		return opponent_move # draw
	elif (needed_outcome == 6): # wins
		if (opponent_move == 'rock'):
			return 'paper'
		elif (opponent_move == 'paper'):
			return 'scissors'
		elif (opponent_move == 'scissors'):
			return 'rock'
	elif (needed_outcome == 0): # losses
		if (opponent_move == 'rock'):
			return 'scissors'
		elif (opponent_move == 'paper'):
			return 'rock'
		elif (opponent_move == 'scissors'):
			return 'paper'

	raise ValueError("Undefined scenario for opponent playing \"" + opponent_move + "\"")

opponent_moves = {
	'A': 'rock',
	'B': 'paper',
	'C': 'scissors'
}

player_moves = {
	'X': 'rock',
	'Y': 'paper',
	'Z': 'scissors'
}

outcomes = {
	'X': 0,
	'Y': 3,
	'Z': 6
}

move_points = {
	'rock': 1,
	'paper': 2,
	'scissors': 3
}

score_style1 = 0
score_style2 = 0
for round in rounds:
	opponent_move = opponent_moves[round[0]]
	player_move = player_moves[round[1]]
	needed_outcome = outcomes[round[1]]
	#print(opponent_move + " :: " + player_move)
	score_style1 += move_points[player_move] + play_style1(opponent_move, player_move)
	score_style2 += needed_outcome + move_points[play_style2(opponent_move, needed_outcome)]

print("Player score (style 1): " + str(score_style1))
print("Player score (style 2): " + str(score_style2))
