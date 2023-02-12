from . import card

class User():
    def __init__(self, name, cards,level):
        self.name = name
        self.cards = cards
        self.level = level
        

    def modifyCard(curr_card, newLimit):
        curr_card.setLimit(newLimit)


