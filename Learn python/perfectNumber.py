#the perfect number is a sum of all factor  of that number is equal to that number is known as perfect number

n = int(input("Enter number:")
)
l=[]
result =0
def factor_check(n):
    
    i = 1
    while i<n:
      if n % i ==0:
        l.append(i)
      i +=1    
    return l


factor_check(n) 

for i in l:
   result +=i

if result == n:
   print("Its a perfect number")
else:
   print("Its not a perfect number")