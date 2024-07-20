n = int(input())

tong = 0

while n != 0:

    s = n % 10

    tong += s

    n //= 10
    
print(tong)