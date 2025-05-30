
num = int(input("enter number:"))


# # def  toFindFectorial(num):
# #     if num == 0 or num ==1:
# #         return 1
# #     else:
# #         return num*toFindFectorial(num-1)

# # result = toFindFectorial(num)
# # print(result)    


#                           # without using recursion
fect = 1
i =1
while i<=num:
    fect *= i
    i +=1
    
print(fect)    


# def fec(num):
#     if num == 0:
#         return 1
#     return num*fec(num-1)

# num = int(input("Enter number to get Fectorial : "))
# for i in range(num+1):
#     print(f"Factorial of {i} is : {fec(i)}")
num2= input("enter number:")
print(num2.count('7'))