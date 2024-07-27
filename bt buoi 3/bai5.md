def so_cuoi(n):

    k = n % 10

    return k

if __name__ == '__main__':

    n = int(input())

    a = list(map(int,input().split()))

    dem = 0

    q = []

    for x in a:

        if so_cuoi(x) == 1 or so_cuoi(x) == 3 or so_cuoi(x) == 5 or so_cuoi(x) == 7 or so_cuoi(x) == 9:

            q.append(x)

            dem += 1

    q.sort()

    print(dem)
    
    print(q)
