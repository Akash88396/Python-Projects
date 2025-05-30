# Example
# Input : number = 5
# Output : It's an Automorphic number.
# Explanation : Number = 5
# Square of number = 25
# as the square of the number ends with the number itself, It's an Automorphic number.

num = int(input("Enter number:"))

def square(num):
    return num * num

result =str(square(num))
 

if result[-len(str(num)):] == str(num):# Ye slice karta hai last 2 characters (because -2: means “2 from end to end”).
    print("Its a Automorphic number.")
else:
    print("Its not aAutomorphic number.")

