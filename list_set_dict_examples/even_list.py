'''
Given a list of numbers, write a Python program to print all even numbers in the given list.

Example: 

Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]
'''

list1 = [2, 7, 5, 64, 14]
list2 = []

for item in list1:
    if item %2 == 0 :
        list2.append(item)

print("even list is: ", list2)