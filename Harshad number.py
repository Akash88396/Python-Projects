# Example
# Input : 21
# Output : Yes ' It's a Harshad Number.
# Explanation : The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.

num = input("Enter number :")

def sum(nu):
    s =0
    for i in nu:
        s=s+int(i)
        
    return s    

result =sum(num)

if int(num) % result == 0:
    print("its a harshad number")
else:
    print("its  not a harshad number")