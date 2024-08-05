a = tuple(map(int,input().split()))
dem = 0
k = 0
for x in a:
    if x in a:
        dem += 1
        if dem % 5 == 0 and dem % 10 != 0:
            print(x)
