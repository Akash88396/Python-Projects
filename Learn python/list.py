l1 = ["Akash",85,True,8.22]
#print(type(l1))

for i in l1:
    print(i, end = " ")

# we can take input from user in run time using import ast

import ast

l1 = ast.literal_eval(input("Enter list  in 1 :"))
l2 = ast.literal_eval(input("Enter list  in 2 :"))
l  = l1+l2
print(l[2])
