# Question: n ka input lo aur squares ka list banao using list comprehension.


# n = int(input("Enter number:"))
# square_list = [i**2 for i in range(1,n+1)]
# print(square_list)


# Question: Ek list di gayi hai, usme se sirf even numbers ka list banao.   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers =[i for i in range(len(numbers)) if i%2 == 0 ]
# print(numbers)


#Question: Do lists di gayi hain, common elements ka list banao.


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# listCommon = [x for x in list1  if x in list2]
# print(listCommon)


# Question: Ek string di gayi hai, sirf vowels ko extract karo.


# text = "hello world"

# test = [x for x in text if x in ('a','e','i','o','u')]
# print(test)



#Question: Ek list of strings di gayi hai, har string ko reverse karo aur uppercase me convert karo

# words = ["apple", "banana", "cherry"]
# words = [ x[::-1].upper() for x in words]
# print(words)



#Question: Ek dictionary banao jisme keys 1 se n tak hon aur values unka square ho.

# n = int(input("Enter number:"))
# dicsquare = { i: i**2 for i in  range(1 , n +1)}
# print(dicsquare)

# Question: Ek list di gayi hai, duplicates hatao aur sorted list return karo.
# nums = [3, 1, 2, 3, 4, 2, 1, 5]
# num = sorted(set(nums))
# print(num)







# Step 1: Input lena
n = int(input())  # Number of scores
arr = list(map(int, input().split()[:n])) # List of scores

# Step 2: Unique scores nikalna
unique_scores = list(set(arr))  # Set se duplicates remove

# Step 3: Sorting karna
unique_scores.sort(reverse=True)  # Descending order me sort

# Step 4: Second highest print karna
print(unique_scores[1])  # Runner-up score










