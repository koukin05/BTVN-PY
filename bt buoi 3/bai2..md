import numpy as np

k = int(input())

a = list(map(int,input().split()))

n,m = map(int,input().split())

if n * m > k:

    print("NO")

yasuo = np.array(a)

zed = yasuo.reshape(n,m)

print(zed)
