"""
@prob_name
Print

@prob_qs
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n

@prob_link
https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

@constraint
1 <= n <= 150
"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(1,n+1):
        print(i, end='')