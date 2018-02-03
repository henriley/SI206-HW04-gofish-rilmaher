import random
import unittest

# SI 206 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Wednesday 9:00am
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)
	def deal(self, num_hands, num_cards):
		list_hands = []
		deck = Deck()
		for x in range(num_hands):
			list_hands += [[x]]
		print(list_hands)
		for x in list_hands:
			if len(x) < num_cards:
				x += [deck.pop_card()]
deck = Deck()
print(deck.deal(4,7))
class  Hand(Deck):
    #creates the Hand with an initial set of cards
    #param: list of cards
    def __init__(self, init_cards):
        self.init_cards = init_cards #sets the hand to the list of cards passed in as a parameter

    #add a card to the hand
    #silently fails if the card is already in the hand
    #param: the card to add
    #returns: nothing
    def add_card(self, card):
        card_strs = [] #forming an empty list
        for c in self.init_cards: # each card in self.init_cards (the initial hand)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.init_cards.append(card) # append it to the list

    #removes a card from the hand
    ##params: the card to remove
    #returns: the card, or None if the card was not in the hand
    def remove_card(self, init_cards, card):
        if card in init_cards:
            init_cards.remove(card)
            return card
        else:
            return None

    #draw a card from the deck and add it to the hand
    #side effect: the deck will be depleted by one card
    #returns: nothing
    def draw(self, init_cards, deck):
        card = deck.pop_card()
        card_strs = []
        if card not in card_strs:
            self.init_cards.append(card)

	# def remove_pairs(self, init_cards):
	# 	list_to_remove = []
	# 	for x in init_cards:
	# 		if init_cards.rank.count(2):
	# 			list_to_remove += x
	# 	sorted_init_list = sorted(init_cards, key = lambda x: x.rank)
	# 	sorted_list_to_remove = sorted(list_to_remove, key = lambda x: x.rank)
	# 	for x in init_cards:
	# 		if x in list_to_remove:
	# 			init_cards.pop(x)

def play_go_fish_game():
    new_deck = Deck()
    deck = deck.shuffle()
    p1_cards = deck.deal(1, 7)
    p2_cards = deck.deal(1, 7)
    p1_score = 0
    p2_score = 0

	print("\n*** BEGIN THE GAME ***\n")

    while True:
        if p1_cards == []:
            break
        if p2_cards == []:
            break
        p1_input = input("Player 1, please choose a card rank you would like to ask the other player if they have. It must be a suit you have.")
        for x in p2_cards:
            if int(p1_input) == x.suit:
                print("Player 1 wins a point!")
                p1_score += 1
                continue

        else:
            print("Go Fish")
            p1_cards += deck.pop(1,1)

            if p1_cards == []:
                break
            if p2_cards == []:
                break
        while True:
            if p1_cards == []:
                break
            if p2_cards == []:
                break
            p2_input = input("Player 2, please choose a card rank you would like to ask the other player if they have. It must be a suit you have.")
            for x in p1_cards:
                if int(p1_input) == x.suit:
                    print("Player 2 wins a point!")
                    p2_score += 1
                    continue

                else:
                    print("Go Fish")
                    p1_cards += deck.pop(1,1)
                    break

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")

print (play_go_fish_game())
