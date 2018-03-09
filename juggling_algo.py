
from math import gcd
def array_left_rotate(arr, d, n):
    """
    this id a method of array rotation by d elements
    time complexity : O(n)
    space complexity: O(1)
    """
    for i in range(gcd(n, d)):
        temp = arr[i]
        for j in range(i, n, d):   
            if ((j + d) % n != i):
                arr[j] = arr[(j + d) % n]
            else:
                arr[j] = temp
                break
    

# UTILITY FUNCTION
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    d = 3
    n = 9
    array_left_rotate(arr, d, n)
    print_array(arr)