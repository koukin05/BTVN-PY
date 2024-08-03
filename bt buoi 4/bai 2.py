n = map(int,input().split())
m = map(int,input().split())
a = set(n)
b = set(m)
if a & b:
    print('YES')
else:
    print('NO')
print(a.union(b))
print(a - b)