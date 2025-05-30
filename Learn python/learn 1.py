
"""

#name = input("What is name: ")

age = int(input("What is age:"))#ager type cast nhi kroge to age me strin jayga "990" ye string hai isko type cast krke int  me kiya haio

# print(type(age))
print(1091 - age)
# Two strings are connected with + operator

#print("Your name is " + name + " and your age is " + age)

Multi line code 

"""
# print("\"HI \nAkash yadav\" \n \'And i want to meetup you\'")# its all are escape sequence 
# print("hey",3,2,sep="#")# sep is a parameter to use seprate the word 
# print("Hi akash yadav ",end = "Its all done")# end parameter use to write the content at the end of the statement 

# print(1+1)
# print(2-1)
# print(42/2)
# print(42//4)
# print(2**2)
# print(2*2)

    

# import ast 

# li = ast.literal_eval(input("Enter list1:"))

# for i in li:
#     if i[0].upper() == "A" and i[-1].upper() =="A":
#         print(i)

import numpy as np 
# l = np.linspace(1, 15, 7
#                 )  # 5 values from 0 to 1
# print(l)
# print(type(l))

# a = np.array([0 ,1 ,2 ,3 ,4, 5 ,6, 7 ,8, 9])
# print(a)


# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.reshape(3,2))
# print("Shape:", arr.shape)  # (2, 3) → 2 rows, 3 columns



# a = np.arange(16)
# print("Original:", a)
# print("Shape:", a.shape)

# b = a.reshape(4, 4)
# print("Reshaped to 4x4:\n", b)

# c = a.reshape(2, 8)
# print("Reshaped to 2x8:\n", c)

# arr2d = np.array([[1, 2, 3], [4, 5, 6]])
# arr1d = np.array([10, 20, 30])

# result = arr1d + arr2d  # arr1d is broadcast to each row of arr2d
# print(result)



# arr1 = np.array([1, 2, 3])
# arr2 = np.array([[1, 2], [3, 4]])
# result = arr1 + arr2 # Error: Shapes are not aligned
# print(result)



# Random integers between 0 and 9
#rand_ints = np.random.randint(0, 10, size=5)
# rand_ints = np.random.random(5)
# print(rand_ints)  # Example output: [2 8 3 9 5]

# rand_uniform = np.random.uniform(low=0, high=10, size=5)
# print(rand_uniform)  # Random numbers between 0 and 10

# arr = np.array([1, 2, 3, 4, 5])
# np.random.shuffle(arr)
# print(arr)  # Array shuffled


# import numpy as np

arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)
loaded_arr = np.load('my_array.npy')
print(loaded_arr)  # Output: [1 2 3 4 5]

