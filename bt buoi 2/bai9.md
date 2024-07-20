def F(n):

    if n != 0:

        F(n // 2)

        print(n % 2, end = ' ')

if __name__ == '__main__':

    n = int(input())

    if n == 0:

        print(0)

    else:
    
        F(n)

9 b

x = "awesome"
print("Python is {}".format(x))

x = "awesome"
print("Python is " + x)

x = "awesome"
print("Python is ",x)

9 c

import sys

print(sys.version)
