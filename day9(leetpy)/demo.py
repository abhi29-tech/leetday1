# import heapq

# pq=[]
# heapq.heappush(pq,3)
# heapq.heappush(pq,3)
# heapq.heappush(pq,3)

# print("priority queue",pq)
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))


# import heapq

# pq = []   
# heapq.heappush(pq, (2, "medium task"))
# heapq.heappush(pq, (1, "high task"))
# heapq.heappush(pq, (3, "low task"))

# while pq:
#     priority, task = heapq.heappop(pq)
#     print(priority, task)


# nums = [1, 2, 3, 5]
# n = len(nums) + 1
# expected = n * (n + 1) // 2
# actual = sum(nums)
# print(expected - actual)

# 83(REMOVE DUPLICATE)
# nums = [1, 1, 2, 3, 3]
# result = []
# for num in nums:
#     if num not in result:
#         result.append(num)
# print("After removing duplicates:", result)


#REVERSE WORD IN STRINGS
s = input("enter the word")
words = s.split(" ")
result = ""
for word in words:
    result = result + word[::-1] + " "
print(result.strip())