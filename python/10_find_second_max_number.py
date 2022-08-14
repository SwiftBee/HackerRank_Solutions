"""
@prob_name
Find Second Max Number

@prob_link
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

@example1
INPUT:
5
2 3 6 6 5

OUTPUT:
5

@constraint
2 <= n <= 10
-100 <= A[i] <= 100

@performance
Time Complexity: O(n) Only one traversal of the array is needed
Auxiliary space: O(1) As no extra space is required
"""

if __name__ == '__main__':
    n = int(input())
    arr = tuple(map(int, input().split()))
    
    first, second = arr[0], float('-inf')
    i = 1
    
    while i < len(arr):
        if arr[i] > first:
            second = first
            first = arr[i]
            
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
        
        i += 1
    
    print(second)