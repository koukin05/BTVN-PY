from math import*

def tong_uoc(n):
    
    tong = 1
    
    for i in range(2, isqrt(n)):
        
        if n % i == 0:
            
            tong += i
            i
            f i != n // i:
                
                tong += n // i
    return tong

if __name__ == '__main__':
    
    n = int(input())
    
    for i in range(1, n + 1):
        
        b = tong_uoc(i)
        
        if b > i and tong_uoc(b) == i:
            
            print(i,b)