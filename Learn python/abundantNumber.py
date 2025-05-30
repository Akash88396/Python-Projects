# Example
# Input : Number = 12
# Output : Yes, It's an Abundant Number
# Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
# Now the sum of the factors except the number itself is :
# 1 + 2 + 3 + 4 + 6 = 16
# as the number 16>12 , the number itself.
# It's an abundant number.

num1 = int(input("Enter number 1:"))


def factor(num):
    lis=[]
    for i in range(1,num):
        if num % i == 0:
            lis.append(i)
    return lis        

l1 =sum(factor(num1))

if l1>num1:
    print("Its a abundant  number ")
else:
    print("its not a abundant number")


