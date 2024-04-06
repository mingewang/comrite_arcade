'''
original at:
https://www.geeksforgeeks.org/python-program-to-find-the-strongest-neighbour/

only compare right neighbor.

Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.
Examples:

Input: 1 2 1 3 4 5
Output:2 2 3 4 5

'''
def maximumAdjacent(arr1):
    # length of arr1
    n = len(arr1)
      # array to store the max 
    # value between adjacent pairs
    arr2 = []  

    # iterate from 0 to n - 1
    for i in range(0, n-1):
        # initial max as this element
        max = arr1[i]
        #print("i is: ", i,  " n is: ", n)
        if max < arr1[i+1]:
            max = arr1[i+1]
        arr2.append(max)    

    return arr2
         
if __name__ == "__main__" :
  # input array
  arr1 = [1,2,2,3,4,5]
  result = maximumAdjacent(arr1)
  print("result is: ", result)