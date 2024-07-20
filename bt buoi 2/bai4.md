def fibo(n):

    if n == 0:

        print(0)

    elif n == 1:

        print('0 1')

    else:

        print('0 1', end = ' ')

        fn1, fn2 = 1,0

        for i in range(2,n):

            fn = fn1 + fn2

            print(fn, end = ' ')

            fn2, fn1 = fn1, fn

if __name__ == '__main__':

    n = int(input())
    
    fibo(n)