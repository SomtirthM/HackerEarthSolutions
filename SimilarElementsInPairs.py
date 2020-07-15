n=int(input())
a=list(map(int,input().split()))

count=0
for i in range(n):
    for j in range(i+1,n):
        if(abs(a[i]-a[j])==1):
            count=count+1
            temp=j
            break
    if(temp==j):
        for k in range(i+1,n):
            if(abs(a[temp]-a[k])==1):
                count=count+1
print(count)
