n = int(input())
a = set(map(int,input().split()))
k = int(input())
a = sorted(a)
b = set()
tong = 0
for x in a:
    if tong + x <= k:
        b.add(x)
        tong += x
print(b)