import sys
sys.setrecursionlimit(100000)
def fibonacci(n):
    a=[None for x in range(n+1)]
    a[0]=0
    a[1]=a[2]=1
    return dinfin(n,a)

def dinfin(n,a):
    if(a[n]==None):
        a[n]=dinfin(n-2,a)+dinfin(n-1,a)
        return a[n]
    return a[n]
print(fibonacci(33000))