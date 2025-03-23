
Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
#Create a python program to sort the given list of tuples based on integer value using a lambda function.
l1 = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
l1.sort(key = lambda l1: l1[1])
print(l1)
[('Virat Kohli', 24936), ('Jack Kallis', 25534), ('Ricky Ponting', 27483), ('Sachin Tendulkar', 34357)]
Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, l2)))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output: ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
#a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tuple(map(lambda x: str(x), l3)))
('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
Q4. Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.
#a python program using reduce function to compute the product of a list containing numbers from 1 to 25.
from functools import reduce
l4=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(reduce(lambda x, y: x*y,  l4))
15511210043330985984000000
Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
#a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.
l5 = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
print(list(filter(lambda x: x%2==0 and x%3==0, l5)))
[6, 60, 90, 120]
Q6. Write a python program to find palindromes in the given list of strings using lambda and filter function.
['python', 'php', 'aba', 'radar', 'level']
#a python program to find palindromes in the given list of strings using lambda and filter function.
l6 = ['python', 'php', 'aba', 'radar', 'level']
print(list(filter(lambda s: s==s[::-1], l6)))
['php', 'aba', 'radar', 'level']
 