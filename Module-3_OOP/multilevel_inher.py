class gfather:
    house=0
    gold=0

    def g_getdata(self):
        self.house=input("Enter house details:")
        self.gold=input("Enter gold details:")

class father(gfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def printdata(self):
        print("House:",self.house)
        print("Gold:",self.gold)
        print('Car:',self.car)
        print("Balance:",self.bal)
    
sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()