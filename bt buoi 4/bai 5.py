n = int(input())
a = []
for i in range(n):
    x = input()
    a.append(x)
b = tuple(a)
print(b)
cnt = 0
for x in b:
    if x.isdigit():
        cnt += 1
print(cnt)