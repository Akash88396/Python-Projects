 # right angle print

line = int(input('Enter number of lines: ')
)
def printRight(line):
    i = 1
    while i <=line:
       print("*" * i)
       i +=1


   
# # by using range function print

# for i in range(1,line):
#     print("*" * i)

                 # opposite right angle

def oppositeRightAngle(line):
    i =line 
    while i >=1 :
        print("*" * i)
        i -=1

                 # left angle trangle print

def leftAngle(line):
    i = 1
    while i<=line:
      print(" " * (line-i) + '*' * i)
      i +=1  

#                     opposite left traingle

def opposteLeftAngle(line):
    i = line
    while i>=1:
        print(" " * (line-i) + "*" * i)
        i -=1

#                               print suare 

def printSquare(line):
    i = 1
    while i <=line:
       print("*" * line)
       i +=1

   
                         # print empty squre

def printEmptySquare(line):
    i =1
    while i<=line:
       if i ==1 or i ==line:
         print("*" * line)     
       else:
        print('*' + ' ' * (line-2) + "*")   
       i +=1  



printRight(line)
#print(" ")
oppositeRightAngle(line)
#print('')
leftAngle(line)
#print('')
opposteLeftAngle(line)
#print('')
printSquare(line)
#print('')
printEmptySquare(line)



