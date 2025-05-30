import numpy as np
# a = np.arange(0,10)
# print(a)
# #[0 1 2 3 4 5 6 7 8 9]
# print(a.shape)
# #(10,) ---> iska matlab hai 10 elements in a single row (1D).
# print(a.ndim)
# # 1  It's a one-dimensional array.
# print(len(a))#Number of elements (same as size for 1D)

 # print(len(a) == a.size)#only on 1d array

# b= np.arange(10)
# print(b)
# print(np.min(b))
# print(np.max(b))
# print(np.mean(b))


# c = np.array([[1,2,3],[4,5,6]])
# print(c.shape)
# print(c.reshape(3,2))


# d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(d.shape)
# print("Column wise minimum value:",np.min(d,axis=0))
# print("Row wise minimum value:",np.min(d,axis=1))

# print('Column wise maximum value:',np.max(d,axis=0))
# print("Row wise mamximum value",np.max(d,axis=1))

# print(np.mean(d))

arr = np.arange(20).reshape(4, 5)
#or
# e = np.array([[1,2,3,4,20],[5,6,7,8,19],[9,10,11,12,18],[13,14,15,16,17]])
print(arr[1:4,3:5])