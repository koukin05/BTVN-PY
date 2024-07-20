a,b,c =  map(int,input().split())

if a + b > c and a + c > b and b + c > a:

    if a == b == c:

        print('day la tam giac deu')

    elif a == b or b == c or a == c:

        print('day la tam giac can')

    elif a ** 2 == b **2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:

        print('day la tam giac vuong')

    else:

        print('day la tam giac thuong')

else:

    print('eo phai tam giac')