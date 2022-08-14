"""
@prob_name
Function

@prob_qs
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

@prob_link
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

@constraint
1900 <= year <= 10^5
"""

def is_leap(year):    
    if (year % 4 == 0 and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))