#10x10 (or some equivalent size grid) where height-row numerical distances are equal
#(do we even need the grid?)

#First throw of the jack is random number generated with row and column [as in battleships, this is not told to the player]
import numpy as np
jack_row = np.random.randint(1,10)
jack_column = np.random.randint(1,10)
"""delete these prints when game runs eventually"""
print jack_row
print jack_column

#coin toss to determine which player throws first (add in case insensitivity with alphanumeric etc down the line)
import random
cointoss = ["heads", "tails"]
print random.choice(cointoss)

user_coin_call=raw_input("Choose heads or tails to determine who throws first")

while true:
	user_coin_call !="heads" and user_coin_call !="tails":
	print "Sorry, you did not select either heads or tails. Please choose again"
	continue

elif raw_input == cointoss:
	print "Congratulations, you won the coin toss. You throw first"
	human_throws=0
	computer_throws=0
	def human_throw(input):
		human_throws+=1
		human_row=raw_input("Guess a row between 0 and 10")
		human_column=raw_input("Guess a column between 0 and 10")
		human_first_throw ="You landed on row %s, column %s(human_row_first, human_column_first)"
	human_throw(input)
	def computer_throw(random number):
		computer_throws+=1
		horizontal=10
		vertical=10
		computer_row=random.choice(horizontal)
		computer_column=random.choice(vertical)
	computer_throw(random number)
	def closest_computation(throws):
		import math
		human_distance_throw=(sqrt(((human_row-jack_row)^2)+((human_column-jack_column)^2))
		computer_distance_throw=(sqrt(((computer_row-jack_row)^2)+((computer_column-jack_column)^2))
		
		if human_distance_throw>=computer_distance_throw and human_throws<3:
			human_throw(input)
			closest_computation
		elif human_distance_throw>=computer_distance_throw and human_throws==3 and computer_throws<3:
			computer_throw(random number)
			closest_computation(throws)
		elif human_distance_throw<computer_distance_throw and computer_throws<3:
			computer_throw(random number)
			closest_computation(throws)
		elif human_distance_throw<computer_distance_throw and computer_throws==3 and human_throws<3:
			human_throw(input)
			closest_computation(throws)
		elif computer_throws==3 and human_throws==3:
			def final_score(throws):


else:
	print "Bad luck, you lost the coin toss. The computer throws first"
	
	




 


#Player turns:
	Throw generated by random row and column, gives distance to jack (known)
	Distance is distance between this point and the jack. So either a horizontal/vertical number if one=same or root of a hypoteneuse if different row and column


#Player turns alternate first throw; thereafter player with closest boule postpones turn until other player gets one closer or runs out of boules


#Winner is player with closest boule after three turns each; number of points scored is number of closest boules before other player has closest
