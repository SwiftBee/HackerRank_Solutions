"""
@prob_name
Finding The Percentage

@prob_link
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

@example1
INPUT:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

OUTPUT:
56.00

@constraint
2 <= N <= 10
0 <= marks[i] <= 100
length of marks arrays = 3
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_marks = student_marks.get(query_name, [])
    print('{:.2f}'.format(sum(query_marks)/len(query_marks)))
    