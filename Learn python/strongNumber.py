num =input("Enter number:")
result =0

def fac(num2):
    if num2 ==0:
        return 1
    return num2*fac(num2-1)

for i in num:
    result +=fac(int(i))

if result == int(num):
    print("Its a strong number")
else:
    print("Not a strong number")    