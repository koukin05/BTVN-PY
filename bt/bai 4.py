n = int(input())
a = [input() for _ in range(n)]
a = list(a)
for x in a:
    x = x.split()
    a = list(x)
    print(a)
