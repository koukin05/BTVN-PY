n, m = map(int,input().split())
a = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happy = 0
unhapy = 99999999999999999999999999999
for x in a :
    if x in A:
        happy += 1
        if x in B:
            happy -= 1
    else:
        happy += 0
print(happy)

