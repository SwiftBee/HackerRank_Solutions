"""
@prob_name
Nested List

@prob_link
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

@example1
INPUT:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

OUTPUT:
Berry
Harry

@constraint
2 <= N <= 5
There will always be one or more students having the second lowest grade
"""

if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
    
    second_lowest = sorted(set(score for _, score in lst))[1]
    print('\n'.join(elem for elem in sorted(name for name, score in lst if score == second_lowest)))