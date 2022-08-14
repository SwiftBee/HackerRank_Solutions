"""
@prob_name
Strict Super Set

@prob_qs
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subse

@prob_link
https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

@example1
set([1,3,4]) is a strict superset of set([1,3]).
set([1,3,4]) is not a strict superset of set([1,3,4]).
set([1,3,4]) is not a strict superset of set([1,3,5]).

@constraint
0 < len(set(A)) < 501
0 < N < 21
0 < len(otherSet) < 101
"""

supset = set(map(int, input().split()))
n = int(input())

for i in range(n):
    subset = set(map(int, input().split()))
    
    if (subset - supset):
        print(False)
        break
    
else:
    print(True)