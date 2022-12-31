class ashok:
    aid=0
    asub=""

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class nirav:
    nid=0
    nsub=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class pratik:
    pid=0
    psub=""

    def p_getdata(self):
        self.pid=input("Enter Pratik's ID:")
        self.psub=input("Enter Pratik's Subject:")

class tops(ashok,nirav,pratik):
    def printdata(self):
        print("------Ashok's Data-----")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("------Nirav's Data-----")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("------Pratik's Data-----")
        print("Pratik's ID:",self.pid)
        print("Pratik's Subject:",self.psub)

tp=tops()
tp.a_getdata()
tp.n_getdata()
tp.p_getdata()
tp.printdata()