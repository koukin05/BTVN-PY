from math import *

def nt(n):

    if n < 2:

        return False

    for i in range(2, isqrt(n) + 1):

        if n % i == 0:

            return False

    return True

def check(n):

    for p in range(2, 35):

        if nt(p):

            if nt(2 ** p - 1):

                if (2 ** p - 1) * (2 ** (p - 1)) == n :

                    return True

    return False

if __name__ == '__main__':

    n = int(input())

    for i in range(1, n + 1):

        if check(i):
        
            print(i, end = ' ')