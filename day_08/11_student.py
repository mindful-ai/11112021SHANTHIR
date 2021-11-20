
# --------------------------------------------  CD
class student:

    # Data
    def __init__(self, name, age, cls):
        # name, age, class, english, maths, science, average, rank
        self.name = name
        self.age = age
        self.cls = cls
        self.english = 0
        self.math = 0
        self.science = 0
        self.average = 0
        self.rank = 0


    # Functions
    def printinfo(self):
        print("This is a student object: ", self)
        print('-'*40)
        print("NAME      : ", self.name)
        print("AGE       : ", self.age)
        print("CLASS     : ", self.cls)
        print('-'*40)
        print("ENGLISH   : ", self.english)
        print("MATHS     : ", self.math)
        print("SCIENCE   : ", self.science)
        print('-'*40)
        print("AVERAGE   : ", self.average)
        print("RANK      : ", self.rank)
        print('-'*40)
        print("\n")


    def calcaverage(self):
        self.average = (self.english + self.math + self.science)/3

    def setmarks(self, sub, marks): # setmarks("eng", 56)
        if sub in ["eng", "mat", "sci"]:
            if(str(marks).isdigit()):
                if(sub == "eng"):
                    self.english = int(marks)
                elif(sub == "mat"):
                    self.math = int(marks)
                else:
                    self.science = int(marks)

                return True
        else:
            return False

    def getaverage(self):
        return self.average

    def assignrank(self, rank):
        self.rank = rank

# --------------------------------------------  AD

s1 = student('Naveen', 10, 5)
#s1.printinfo()
s1.setmarks("eng", 55)
s1.setmarks("mat", 77)
s1.setmarks("sci", 88)
#s1.printinfo()
s1.calcaverage()
s1.printinfo()
#s1.assignrank(1)
#s1.printinfo()

s2 = student('Anil', 10, 5)
#s2.printinfo()
s2.setmarks("eng", 85)
s2.setmarks("mat", 78)
s2.setmarks("sci", 81)
#s2.printinfo()
s2.calcaverage()
s2.printinfo()

s3 = student('Sunil', 10, 5)
#s2.printinfo()
s3.setmarks("eng", 95)
s3.setmarks("mat", 98)
s3.setmarks("sci", 82)
#s2.printinfo()
s3.calcaverage()
s3.printinfo()

# --------------------------------------------------



def ranks(L):
    avgs = []
    for stud in L:
        avgs.append(stud.getaverage())
    print(avgs)
    avgs.sort(reverse=True)
    rank = 1
    for avg in avgs:
        for stud in L:
            if(stud.getaverage() == avg):
                stud.assignrank(rank)
        rank += 1


# --------------------------------------------------

L = [s1, s2, s3]
ranks(L)
s1.printinfo()
s2.printinfo()
s3.printinfo()
