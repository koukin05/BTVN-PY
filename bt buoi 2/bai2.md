a,b = map(int,input().split())

print('a cộng b =',a + b)

print('a trừ b = ',a - b)

print('a nhân b = ',a * b)

print('a mũ b = ',a ** b)

print('a chia dư cho b = ',a % b)

if a > b:

    print("a lớn hơn b")

elif a < b:

    print("a nhỏ hơn b")

else:

    print("a bằng b")

print("a AND b =", a & b)

print("a OR b =", a | b)

print("a XOR b =", a ^ b)

print("NOT a == b =", not (a == b))

print("a dịch phải 1 đơn vị =", a >> 1)

print("a dịch trái 1 đơn vị =", a << 1)