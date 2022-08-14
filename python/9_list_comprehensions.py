"""
@prob_name
List Comprehension

@prob_link
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

@example1
INPUT:
1
1
1
2

OUTPUT:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

@constraint
Print the list in lexicographic increasing order.
"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])
    
    # res = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k != n:
    #                 res.append([i, j, k])    
    # print(res)