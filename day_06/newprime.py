# Project A -> DIfferent approach with functions

# function

'''
def <function name>(<input>):
    <logic>
    return <value>/<expression>
'''

def checkprime(n):
    prime = True
    for i in range(2, n):
        if(n % i == 0):
            prime = False
            break
    return prime

def f1():
    print("Function 1")

'''
def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
'''

# ----------------------------------------------

if __name__ == '__main__':

    def f2():
        print("Function 2")
    
    # input
    n = int(input("Enter a number: "))

    # output
    print('-' * 50)
    if(checkprime(n) == True):
        print("The number is prime")
    else:
        print("The number is not prime")

    f1()
    f2()
