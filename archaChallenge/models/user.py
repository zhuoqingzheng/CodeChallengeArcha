from . import card

class User():
    def __init__(self, name, cards,level,company):
        self.name = name
        self.cards = cards
        self.level = level
        self.company = company
        

    def modifyCard(curr_card, newLimit):
        curr_card.setLimit(newLimit)


