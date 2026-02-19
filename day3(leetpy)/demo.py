# #task1
# #fibonaci

# # n=int(input("enter the number"))
# # a=0
# # b=1
# # for i in range(n):
# #     print(a, end=" ")
# #     a, b = b, a + b

# #tribonaci

# # n=int(input("enter the num:"))
# # a=0
# # b=1
# # c=1
# # for i in range(n):
# #     print(a)
# #     a,b,c=b,c,a+b+c

# #LIST
# #List indices
# a=[1,2,3,6,8,5]
# b=[9,7,8,1]
# print(a[5])
# #list slices
# print(a[1:5])
# print(b[0:])
# #list operators
# #concatination
# print(a+b)
# #repetion
# print(b*4)
# #membership
# name=['abhi','anu','ram','sitha','max']
# print('abhi'in name)
# print('luis'in name)
# #comparision
# print(a==b)
# print(a<b)
# print(a>b)
# #listmethod
# b.append(25)
# print(b)
# #insert
# b.insert(3,67)
# print(b)
# #extend
# a.extend(b)
# print(a)
# #remove
# a.remove(2)
# print(a)
# #pop(index)
# b.pop(0)
# print(b)
# a.clear()
# print(a)
# #index
# print(b.index(8))
# print(b[1])
# count
# print(a.count(2))
# #sort
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# #COPY
# b=a.copy()
# print(b)

# num=[1,2,3,4]
# def func(x):
#     return x*2
# result=list(map(func,num))
# print(result)

# numone=[1,2,3,4,5,6,7,8,9]
# resultone=list(filter(lambda x: x%2==0,numone))
# print(resultone)

# def func(x):
#     return x**2==0
# result=list(filter(func,numone))
# print(result)

#reduce
# from functools import reduce
# num=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,num)
# print(result)


# num=[0,1,2,3,4,5,6,7,8,9]
# result=list(filter(lambda x:x%2==0,num))
# print(len(result))
# print(result)

# palindrome(slicing)
word=input("enter the word:")
if word==word[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# palindrome(without slicing)
# word=input("enter the word:")
# rev=""
# for ch in word:
#     rev=ch+rev
# if word==rev:
#     print("palindrome")
# else:
#     print("not palindrome")





