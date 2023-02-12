class Card():
        def __init__(self,CardNum, expDate, maskedNum, limit, currentBalance, holder):
            self.cardNum = CardNum
            self.expDate = expDate
            self.maskedNum = maskedNum
            self.limit = limit
            self.holder = holder
            self.currentBalance = currentBalance

        def setLimit(self, Limit):
            self.Limit = Limit
        
