from math import*
def nt(n):
    if n < 2 :
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    print(nt(16))