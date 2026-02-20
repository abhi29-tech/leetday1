#CONTAINS DUPLICATE

# def containsDuplicate(nums):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# nums = [1, 2, 3, 1]
# print(containsDuplicate(nums)) 


#COMBINATION
# def combine(n, k, start=1, path=[]):
#     if len(path) == k:
#         print(path)
#         return
#     for i in range(start, n + 1):
#         combine(n, k, i + 1, path + [i])
# combine(4, 2)

#POWER OF TWO
n = int(input("Enter a number: "))

if n <= 0:
    print("False")
else:
    while n % 2 == 0:
        n = n // 2
    
    if n == 1:
        print("True")
    else:
        print("False")

#POWER OF THREE
# n = int(input("Enter a number: "))

# if n <= 0:
#     print("False")
# else:
#     while n % 3 == 0:
#         n = n // 3
    
#     if n == 1:
#         print("True")
#     else:
#         print("False")

#POWER OF FOUR
# n = int(input("Enter a number: "))

# if n <= 0:
#     print("False")
# else:
#     while n % 4 == 0:
#         n = n // 4
    
#     if n == 1:
#         print("True")
#     else:
#         print("False")
        
#OOPS

# class students:
#     def details (self, name, marks):
#         if marks>40:
#             result="pass"
#             print(result)
#             print(name,marks)
#         else:
#             print("fail")
# s1=students()
# s2=students()
# s1.details("abhi",100)    


#SYNTAX (WITHOUT CONSTRUCTAR)
# class ClassName:
#     def method_name(self):
#         print("message")

#WITH CONSTRUCTOR

# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def show_result(self):
#         if self.marks>=40:
#             result="pass"
#         else:
#             result="fail"
#         print("\n Student name:",self.name)
#         print("marks",self.marks)
#         print("result",result)
# name=input("enter name:")
# marks=int(input("enter marks:"))
# s1=student(name,marks)
# s1.show_result()

#
# class TemperatureConverter:
    
#     def __init__(self, celsius_list):
#         self.celsius_list = celsius_list    
#     def convert(self):
#         fahrenheit_list = []        
#         for c in self.celsius_list:
#             f = (c * 9/5) + 32
#             fahrenheit_list.append(f)       
#         return fahrenheit_list    
#     def display(self):
#         fahrenheit_list = self.convert()
#         print("Celsius to Fahrenheit Conversion:")
#         for i in range(len(self.celsius_list)):
#             print(f"{self.celsius_list[i]}°C = {fahrenheit_list[i]}°F")
# celsius_values = [10, 20, 30, 40, 50]
# converter = TemperatureConverter(celsius_values)
# converter.display()

