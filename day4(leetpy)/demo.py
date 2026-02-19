##ANAGRAM

# def isAnagram(s,t):
#     if len(s)!= len(t):
#         return False
#     return sorted(s)==sorted(t)
# s=input("enter 1st word:")
# t=input("enter 2nd word:")
# print("are they anagram?",isAnagram(s,t))

# def numAnagram(s,t):
#     if len(s) != len(t):
#         return False
#     return sorted(s)== sorted(t)
# s=input("enter 1st num:")
# t=input("enter 2nd num:")
# print("are they anagram?", numAnagram(s,t))


# CLIMBING STAIRS
# def climbStairs(n):
#     if n <= 2:
#         return n
    
#     dp = [0] * (n + 1)
    
#     dp[1] = 1
#     dp[2] = 2
    
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
    
#     return dp[n]

# n = 5
# print("number of ways:", climbStairs(n))

#FIZZBUZZ

# def fizzbuzz(n):
#     for i in range (1 , n+1):

#         if i % 15 == 0:
#             print("fizzbuzz")
#         elif i % 3 == 0:
#             print("fizz")
#         elif i % 5 == 0:
#             print("buzz")
#         else:
#             print(i)
# n=int(input("enter num:"))
# fizzbuzz(n)

# Simple Majority Element code
# nums = [2, 2, 1, 1, 1, 2, 2]  

# count = {}
# for num in nums:
#     count[num] = count.get(num, 0) + 1

# majority = max(count, key=count.get)
# print("Majority element is:", majority)

# n=int(input(" enter the num:"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")

# n = int(input("Enter the number: "))

# if n > 0:
#     print("Positive number")
# elif n < 0:
#     print("Negative number")
# else:
#     print("Number is zero")

#lenght of word
# s = input("Enter a string: ").strip()  
# words = s.split()  
# if words:
#     print("Length of last word:", len(words[-1]))
# else:
#     print("Length of last word: 0")

#intersection of two array

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]
# intersection = list(set(nums1) & set(nums2))

# print("Intersection:", intersection)

# #union of two array
# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2, 3]
# union = list(set(nums1))
# for num in nums2:
#     if num not in union:
#         union.append(num)

# print("Union:", union)

#merge sorted array
# nums1 =[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3
# i=m-1
# j=n-1
# k=m+n-1

# while i>=0 and j>=0:
#     if nums1[i]>nums2[j]:
#         nums1[k]=nums1[i]
#         i-=1
#     else:
#         nums1[k]=nums2[j]
#         j-=1
#     k-=1
# while j>=0:
#     nums1[k]=nums2[j]
#     j-=1
#     k-=1
# print (nums1)            


#SINGLE NUMBER
# nums = [4, 1, 2, 1, 2]  

# result = 0
# for num in nums:
#     result ^= num

# print(result)

#LONGEST COMMON PREFIX
# strs = ["flower", "flow", "flight"]  # change the list as needed

# if not strs:
#     prefix = ""
# else:
#     prefix = ""
#     for chars in zip(*strs):
#         if all(c == chars[0] for c in chars):
#             prefix += chars[0]
#         else:
#             break

# print(prefix)


#ADD DIGIT

# num = 38  
# while num >= 10:
#     temp = 0
#     while num > 0:
#         temp += num % 10
#         num //= 10
#     num = temp
# print(num)

#SAME TREE
# p=[1,2,4]
# q=[1,2,4]
# if p==9:
#     print("its same tree")
# else:
#     print("its not")
