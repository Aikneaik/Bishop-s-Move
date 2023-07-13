#Bishop's Move
a1, b1, a2, b2 = int(input()), int(input()) , int(input()) , int(input())

a3 = a2 - a1
b3 = b2 - b1

if a3 == b3  or -a3 == b3 or a3 == -b3: 
    print('YES')
else:
    print('NO')  