# DEck consists of a list of cards as an attribute.

class Card(object):
	''' Class card to represent a playing card '''
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '1', '2', '3', '4', '5', '6', '7', '8',
		'9', '10', 'Jack', 'Queen', 'King']

	def __init__(self, suit = 0, rank = 2):
		self.suit = suit
		self.rank = rank
	
	def __str__(self) :
		return 'Suit : %s  Rank : %s' % (Card.suit_names[self.suit],						Card.rank_names[self.rank])

class Deck(object):
	''' is a list of cards '''
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1,15):
				card = Card(suit,rank)
				self.cards.append(card)

	def __str__(self):	
		res = []
		for card in self.cards:
			res.append( str(card))
		return '\n'.join(res)

	''' to remove a particular card from the deck '''
	def pop_card(self):
		return self.cards.pop()

	''' to add a new card into the existing deck '''
	def add_card(self,card):
		self.cards.append(card)

	''' To shuffle a deck of cards '''
	def shuffle(self):
		import random
		random.shuffle(self.cards)

dck = Deck()
print dck

dck.pop_card()
print dck

new_card = Card(0,2)
dck.add_card(new_card)

print dck

dck.shuffle()
print dck
