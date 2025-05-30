# num = input("Enter number :")
# numLenght = len(num)
# d = 0

# i=0
# while i<numLenght:
#     d += int(num[i])**numLenght
#     i+=1

# if d == int(num):
#     print(f'{num} is a Armstrong number')
# else:
#      print(f'{num} is not a Armstrong number')


#             find armstrong number in given range

# startingNum =int(input("Enter starting point:"))#5
# endingNum =int(input("Enter ending point:"))#16

# found =0

# i = startingNum
# while i<=endingNum:
#     num_str = str(i)
#     num_str_leng = len(num_str)

#     d = 0

#     for digit in num_str:
#         d += int(digit)**num_str_leng
    
#     if d == i:
#         print(f"{i} is a armstrong number")
#         found =1
    
#     i +=1

# if found ==0:
    
#     print(f" There is no armstrong number between {startingNum} and {endingNum} ")



                         # now using range function to find


startingNum =int(input("Enter starting point:"))
endingNum =int(input("Enter ending point:"))
found =0

for i in range(startingNum, endingNum+1):
    num_str = str(i)
    num_str_leng = len(num_str)
    d=0

    for digit in num_str:
        d += int(digit)**num_str_leng
    if d ==i:
        print(f"{i} is a armstrong number")    
        found =1
if(found ==0):
            print(f" There is no armstrong number between {startingNum} and {endingNum} ")