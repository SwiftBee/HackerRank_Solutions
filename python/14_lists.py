"""
@prob_name
Lists

@prob_link
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

@example1
INPUT:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

OUTPUT:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

@constraint
The elements added to the list must be integers
"""

if __name__ == '__main__':
    N = int(input())
    
    lst = []
    for _ in range(N):
        command, *values = input().split()
        values = tuple(map(int, values))
        
        if command == 'insert':
           lst.insert(*values)
        
        elif command == 'print':
            print(lst)
            
        elif command == 'remove':
            lst.remove(*values)
            
        elif command == 'append':
            lst.append(*values)
            
        elif command == 'sort':
            lst.sort()
            
        elif command == 'pop':
            lst.pop()
            
        elif command == 'reverse':
            lst.reverse()