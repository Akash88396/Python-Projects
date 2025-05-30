# input_str = '#mbuamnbdaria'
# output_str = input_str[1: : 2] + " " +  input_str[2: : 2]
# print(output_str)

#                   CHecking the is palimdrom or not 

# #str = input("Enter any string to check palindrome :")
# str = input("Enter any string to check palindrome: ").lower().replace(" ", "")
# str1 = str[: : -1]

# if( str == str1):
#     print( str + " Its a palindrome ")
# else:
#     print( str+ " Its not a palindrom") 



#            WAP to check number is kaprekar number or not 


# c =0 
# a = input("Enter number :")
# b = str(int(a)**2)
# d = len(b)//2

# if(len(b) %2 != 0):
#     c = int(b[ : d+1]) + int(b[d:])
# else:
#     c = int(b[:d]) + int(b[d:])

# if(c == int(a)):
#     print("Its a kaprekar number")
# else:
#     print("Its not a kaprekar number")


#              WAP to remove first and last letter of string

# str = input('ENTER string:')

# if len(str)>1:
#     result = str[1:-1]
# else:
#     result = "String is too short"

# print("Result is : " , result)    



#          WAP to count the occurance of letter "a" in a string = 'aadbaaaabdcdabdadabda'  without using count function


# str = 'aadbaaaabdcdabdadabda'
# count = 0
# for i in str:
#     if(i == 'a'):
#         count = count +1


# print("Occurence of a is : ", str.count("a"))# by using function
# print("Occurence of a is : ", count)# by using for loop


#            WAP to check number is divisible by 3 and 5 or not

# num = input("Enter number:")
# three = 0
# for i in num:
#     three = three + int(i)

#simply you can

## if num % 3 ==0 and num % 5 ==0:
##    print()
## else:
##    print()


# if three % 3 == 0 and int(num[-1]) == 0 or int(num[-1]) == 5:
#     print( num , "  is divided by both 3 and 5")
# else:
#     print(num , " is not divided by both 3 and 5")


# WAP to check number is prime or not

# num = int(input("Enter number:"))
# mark =0
# for i in range(2,num):
#     if num % i == 0:
#         mark =1
#         break
        
# if(mark == 1):
#     print(num," Its prime number")
# else:
#      print(num, " Its not prime number")



#                          print right angle traingle


