"""
@prob_name
Lists

@prob_qs
Given an integer, n, and n space-separated integers as input, create a tuple, t, of n those  integers. Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

@prob_link
https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

@example1
INPUT:
2
1 2

OUTPUT:
3713081631934410656
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))