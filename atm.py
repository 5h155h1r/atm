class ATM(object):
    def __init__(self, cardNum, pin):
        self.cardNum = cardNum
        self.pin = pin
        self.balance  = 300
    
    def checkBalance(self):
        print("Your accont has a balance of $300")
    def withDraw(self):
        moneyWith = int(input("Select amount to withdraw"))
        self.balance = self.balance - moneyWith
        print("Here is your money $$$")
        print("Remaining balance is "+ str(self.balance))
    

account1 = ATM("1234", "1234")
account1.checkBalance()
account1.withDraw()