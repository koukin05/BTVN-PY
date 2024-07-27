n = int(input())

a = list(map(int,input().split()))

x = int(input())

print(a.count(x))

a[2:7] = [8,5,4,0,1,3]

print(a)

print(max(a))

print(min(a))

y = int(input())

a.insert(0, y)

print(a)

b = sorted(a)

if b == a:

    print("TANG")

elif b == a.reverse():

    print("GIAM")

else:

    print("NO")

e = []

for i in range(1, len(a) + 1):

    yasuo = sum(range(1,i + 1))

    e.append(yasuo)

print(e)

no_hope = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]

no_hope.sort()

print(no_hope)

no_hope.sort(key = abs)

print(no_hope)


