# Program to determine if the result is positive, negative or zero
# after subtraction

# input
a = input("Enter the first number: ")
b = int(input("Enter the second number: "))
a = int(a)

# process
res = a - b

# output
print('-'*50)

if(res > 0):
    print("The number is positive")
elif (res < 0):
    print("The number is negative")
else:
    print("The number is zero")

    
