#PASCALS TRIANGLE
# numRow = int(input("Enter number of rows: "))
# triangle = []
# for i in range(numRow):
#     row = [1] * (i + 1)
#     for j in range(1, i):
#         row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#     triangle.append(row)
# for row in triangle:
#     print(row)
    

#ROMAN TO INTEGER

# def roman_to_int(s):
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     values = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50, 
#         'C': 100, 'D': 500, 'M': 1000
#     }
#     total = 0
#     for char in s:
#         total += values[char]
#     return total
# print(roman_to_int("IV"))      
# print(roman_to_int("MCMXCIV")) 

#MAX PRODUCT OF THREE NUMBERS
# def maximumProduct(nums):
#     nums.sort()
#     option1 = nums[-1] * nums[-2] * nums[-3]
#     option2 = nums[0] * nums[1] * nums[-1]
#     return max(option1, option2)
# print(maximumProduct([1, 2, 3]))        
# print(maximumProduct([-10, -10, 5, 2]))   

# def roman_to_int(s):
#     s = s.replace("IV", "IIII").replace("IX", "VIIII")
#     s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#     s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#     values = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50, 
#         'C': 100, 'D': 500, 'M': 1000
#     }
#     total = 0
#     for char in s:
#         total += values[char]
        
#     return total
# print(roman_to_int("IV"))      
# print(roman_to_int("IX"))     
# print(roman_to_int("MCMXCIV"))   

def detectCapitalUse(word):
    if word.isupper():
        return True
    if word.islower():
        return True
    if word.istitle():
        return True
    return False
user_word = input("Enter the word: ")
print("Is it valid?", detectCapitalUse(user_word))












