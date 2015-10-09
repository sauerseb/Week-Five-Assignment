# Evan Sauers 
# GameOfWar2.py
# Game of War Version 2
# Collaborated with Rebekkah and Marissa

import random	

def main():
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
		
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter > 1000:
			print ("The War Game is a draw")
			break
		
	# End of game
	
	print("There were ", gameCounter, " rounds played")
	print("Player A has " + str(len(PlayerAHand)) + "cards, Player B has " + str(len(PlayerBHand)) + "cards")
	
def playRound(PlayerA, PlayerB):
	
	Acard = PlayerA.pop()
	Bcard = PlayerB.pop()
	
	rankA = getRank(Acard)
	rankB = getRank(Bcard)
	
	if rankA > rankB:
		#If Player A wins
		PlayerA.insert(0, Acard)
		
	elif rankB < rankA:
		#If Player B wins
		PlayerB.insert(0, Bcard)
		
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
		
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()



