class Card():
        def __init__(self,CardNum, expDate, maskedNum, limit, currentBalance):
            self.cardNum = CardNum
            self.expDate = expDate
            self.maskedNum = maskedNum
            self.limit = limit
            
            self.currentBalance = currentBalance

        def setLimit(self, Limit):
            self.Limit = Limit
        
