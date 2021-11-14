# Program to determine if a number is prime or not

# Prime number is a number that cannot be divided by any number except
# itself and 1
# Example: 7 is prime, 4 is not prime
# 5 -> divide by 2, 3, 4

# input
n = int(input("Enter a number: "))

# process/output

for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")
