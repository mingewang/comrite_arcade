'''
original at:
https://www.geeksforgeeks.org/python-program-to-find-the-strongest-neighbour/

But change to check left and right neightbor
Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.
Examples:

Input: 1 2 2 3 4 5
Output:2 2 3 4 5 5

'''
def maximumAdjacent(arr1):
    # length of arr1
    n = len(arr1)
      # array to store the max 
    # value between adjacent pairs
    arr2 = []  

    if n <= 1:
        arr2 = arr1
     
    # iterate from 1 to n - 1
    for i in range(0, n):
        # initial max as this element
        max = arr1[i]
        if i == 0:
            # valid i+1
            if i + 1 <= n-1:
                if max < arr1[i+1]:
                    max = arr1[i+1]
        elif i == n-1:  # last element
            if i - 1 >= 0:
                if max < arr1[i-1]:
                    max = arr1[i-1]
        else:
            if max < arr1[i-1]:
                max = arr1[i-1]
            if max < arr1[i+1]:
                max = arr1[i+1]
        arr2.append(max)    

    return arr2
         
if __name__ == "__main__" :
   
  # input array
  arr1 = [1,2,2,3,4,5]
  result = maximumAdjacent(arr1)
  print("result is: ", result)