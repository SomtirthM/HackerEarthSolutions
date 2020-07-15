n=int(input())
lst=list(map(int,input().split()))
res=[]
p=0
for i in range(len(lst)-1,-1,-1):
        if lst[i]>=p:
                res.append(lst[i])
                p=lst[i]
res.reverse()
for k in res:
        print(k,end=" ")
