#                         if statement

# a = int(input("Enter number to check the number is even or not :"))
# if(a%2==0):
#     print( a , "is an even number.")

#                         if else stement 


# a = int(input("Enter number to  check number is even or odd: "))

# if(a%2 == 0):
#     print(a , "is even number.")
# else:
#     print( a ,"Number is odd.")    


#                        nested if else ledder


# a= int(input("Enter first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the thired  number:"))

# if(a>b and a>c):
#     print(a, "is grater ")
# else:
#     if(b>a and b>c):
#        print(b , " is grater")
#     else:
#         print(c , " is grater.")


b = [1,2,3,4,2]

# for i in b:
#     print(i,end = 6)

# i = 2
# while i<10:
#     print(i)
#     i+=1
    
day = int(input("Enter number from 1 to 7 to get day:"))

match (day):
     case 1:
        print("Monday")
    
     case 2:
        print("Tuesday")
        
     case 3:
        print("Wednesday")
     case 4:
        print("Thursday")
     case 5:
        print('Friday')
     case 6:
        print("Saterday") 
     case 7:
        print("Sunday")    
      
       

        