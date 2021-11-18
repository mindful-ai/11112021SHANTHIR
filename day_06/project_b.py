# Project B

# Input a few numbers from the user
# Separate out all the even, odd and prime numbers from them

import newprime

# input
# 3, 10, 23, 34, 65, 78, 89, 7 .... q

'''
uin = ''
while uin != 'q':
    <statements>
'''

n = []
while True:
    uin = input("# ")
    if(uin.lower()[0] == 'q'):
        break
    else:
        if(uin.isdigit()):
            n.append(int(uin))

print(n)

# process

evens = []
odds = []
primes = []

for num in n:
    if(num % 2 == 0):
        evens.append(num)
    else:
        odds.append(num)

for num in n:
    if(newprime.checkprime(num) == True):
        primes.append(num)

# output
# E -> 10, 34, 78...
# O -> 3, 23, 65, 89, 7...
# P -> 3, 7

print("-"*60)
print("ODDS   : ", odds)
print("EVENS  : ", evens)
print("PRIMES : ", primes)

newprime.f1()
newprime.f2()
