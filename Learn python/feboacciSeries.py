num = int(input("Enter number:"))
# a =0
# b =1

# i =0
# while i<=num:
#     print(a,end=" ")
#     c =a+b
#     a =b
#     b=c

#     i+=1
    
              # by using for loop  to find febonacci series 
a =0 
b =1

for i in range(num+1):
    print(a, end=" ")
    c = a+b
    a = b
    b=c
                  