import random

suits=('♥','♣','♦','♠')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True

class Card():
	def __init__(self,suits,rank):
		self.suits=suits
		self.rank=rank

	def __str__(self):
			return self.rank+" of "+self.suits

class Deck():
	def __init__(self):
		self.deck=[]
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	
	def __str__(self):
		deckComp=''
		for card in self.deck:
				deckComp+='\n'+card.__str__()	
		return "The deck has: "+deckComp		

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		singleCard=self.deck.pop()
		return singleCard	
		
class Hand():
	def __init__(self):
		self.cards=[]
		self.value=0
		self.aces=0


	def addCard(self,card):
		self.cards.append(card)
		self.value+=values[card.rank]

		if card.rank=='Ace':
			self.aces+=1

	def adjustForAce(self):
		while self.value>21 and self.aces>0:
			self.value-=10
			self.aces-=1


class Chips(object):
	def __init__(self,total=100):
		self.total=total
		self.bet=0

	def winBet(self):
		self.total+=self.bet
		
	def loseBet(self):
		self.total-=self.bet


def takeBet(chips):
	while True:
		try:
			chips.bet=int(input("How many chips would you like to bet? "))	
		except ValueError:
			print("Sorry please provide an integer")
		else:
			if chips.bet>chips.total:
				print("Sorry, you do not have enough chips! You have {}".format(chips.total))
			else:
				break
			
def hit(deck,hand):
	singleCard=deck.deal()
	hand.addCard(singleCard)
	hand.adjustForAce()

def hitOrStand(deck,hand):
	global playing

	while True:
		x=input("Hit or Stand? Please enter h or s ")

		if x[0].lower()=='h':
			hit(deck,hand)
		elif x[0].lower()=='s':
			print("Player Stands Dealer's turn")
			playing=False	
		else:
			print("Sorry, I did no understand that, Please enter h or s only!!")
			continue

		break

def showSome(player,dealer):
	print("DEALERS HAND: ")
	print("one card hidden!")
	print(dealer.cards[1])
	print("\n")
	print("PLAYERS HAND: ")
	for card in player.cards:
		print(card)

def showAll(player,dealer):
	print("DEALERS HAND: ")
	for card in dealer.cards:
		print(card)
	print("\n")
	print("PLAYERS HAND: ")
	for card in player.cards:
		print(card)

def playerBusts(player,dealer,chips):
	print("BUST PLAYER!")
	chips.loseBet()

def playerWins(player,dealer,chips):
	print("PLAYER WİNS!")
	chips.winBet()

def dealerBusts(player,dealer,chips):
	print("PLAYER WİNS! DEALER BUSTED!")
	chips.winBet()

def dealerWins(player,dealer,chips):
	print("DEALER WINS!")
	chips.loseBet()

def push(player,dealer):
	print("Dealer and Player tie! PUSH")


while True:
	print("Welcome to BlackJack")

	deck=Deck()
	deck.shuffle()

	playerHand=Hand()
	playerHand.addCard(deck.deal())
	playerHand.addCard(deck.deal())

	dealerHand=Hand()
	dealerHand.addCard(deck.deal())
	dealerHand.addCard(deck.deal())

	playerChips=Chips()

	takeBet(playerChips)

	showSome(playerHand,dealerHand)

	while playing:
		hitOrStand(deck,playerHand)

		showSome(playerHand,dealerHand)

		if playerHand.value>21:
			playerBusts(playerHand,dealerHand,playerChips)
			break
	if playerHand.value<=21:
		while dealerHand.value<playerHand.value:
			hit(deck,dealerHand)


			showAll(playerHand,dealerHand)

			if dealerHand.value>21:
				dealerBusts(playerHand,dealerHand,playerChips)
			elif dealerHand.value>playerHand.value:
				dealerWins(playerHand,dealerHand,playerChips)
			elif dealerHand.value<playerHand.value:
				playerWins(playerHand,dealerHand,playerChips)
			else:
				push(playerHand,dealerHand)


	print("\n Player total chips are at: {}".format(playerChips.total))

	newGame=input("Would you like to play another hand? y/n")

	if newGame[0].lower()=='y':
		playing=True
		continue
	else:
		print("Thank you for playing!")
		break

		

