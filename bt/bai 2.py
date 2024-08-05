n = int(input())
so_buoc = 0
if (n + 1) % 3 == 1:
    so_buoc = (n // 3) + 1
elif (n + 1) % 3 == 2:
    so_buoc = (n // 3) + 1 
elif (n + 1) % 3 == 0:
    so_buoc = n // 3
print(so_buoc)