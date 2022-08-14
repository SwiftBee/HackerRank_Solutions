"""
@prob_name
Loops

@prob_link
https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true

@constraint
1 <= n <= 20
"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)