# Program to determine if a number is prime or not

# Prime number is a number that cannot be divided by any number except
# itself and 1
# Example: 7 is prime, 4 is not prime
# 5 -> divide by 2, 3, 4

# input
n = int(input("Enter a number: "))

# process
prime = True
for i in range(2, n):
    if(n % i == 0):
        prime = False
        break

# output
print('-' * 50)
if(prime == True):
    print("The number is prime")
else:
    print("The number is not prime")

    

