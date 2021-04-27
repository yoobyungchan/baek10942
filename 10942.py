import sys
t = int(input())
a = [int(i) for i in sys.stdin.readline().split()]
n = int(input())
d = [[0]*t for _ in range(t)]
for i in range(t):
    d[i][i] = 1

for i in range(t-1):
    if a[i] == a[i+1]:
        d[i][i+1] = 1

for i in range(t-3, -1, -1):
    for j in range(i+2,t):
        if d[i+1][j-1] == 1 and a[i] == a[j]:
            d[i][j] = 1

for i in range(n):
    x, y = [int(a) for a in sys.stdin.readline().split()]
    print(d[x-1][y-1])
