num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

def factor(num):
    lis=[]
    for i in range(1,num):
        if num % i == 0:
            lis.append(i)
    return lis        

l1 =sum(factor(num1))
l2 = sum(factor(num2))

if l1/num1 == l2/num2:
    print("Its a friendly pair number ")
else:
    print("its not a friendly pair number")


