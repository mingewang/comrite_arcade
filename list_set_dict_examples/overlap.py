'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = []


if len(a) < len(b):
    for num in a:
        if num in b:
            print(num)
            if num not in result:
                result.append(num)
else: 
    for num in b:
        if num in a:
            print(num)
            if num not in result:
                result.append(num)
                
print("final overlapped list is: ", result)