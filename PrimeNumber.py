num = int(input("Enter number:"))

flag = 0
             
                              # using range funtion

for i in range(2,num):
    if num % i == 0:
        flag =1
        break
if flag == 1:
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")

