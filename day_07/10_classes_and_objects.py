class myfunctions:

    def __init__(self, extval):
        self.a = extval
        print(self)

    def add5(self):
        return self.a + 5

    def sub5(self):
        return self.a - 5

    def mul5(self):
        return self.a * 5

    def div5(self):
        return self.a / 5

# --------------------------------------



x = myfunctions(10)
print(x, x.add5(), x.sub5(), x.mul5(), x.div5() )


y = myfunctions(100)
print(y.add5(), y.sub5(), y.mul5(), y.div5() )
print(x.add5(), x.sub5(), x.mul5(), x.div5() )

L = list(range(10, 20))
objs = []
for i in L:
    objs.append(myfunctions(i))

print(objs)


for obj in objs:
    print(obj.add5())
