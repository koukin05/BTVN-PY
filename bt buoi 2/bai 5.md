def checkarm(n):
    
    temp = n
    
    k = 0
    
    while n != 0:
        
        s = n % 10
        
        a = s ** 3
        
        k += a
        
        n //= 10
    
    return k == temp

if __name__ == '__main__':
    
    n = int(input())
    
    for i in range(1,n + 1):
        
        if checkarm(i):
           
            print(i, end = ' ')