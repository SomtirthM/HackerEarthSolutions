k = int(input())
for _ in range(n):
    le,n  = map(int,input().split())
    array = list(map(int,input().split()))
    x = n-min(array)
    if x>0:
        print(x)
    else:
        print(0)
