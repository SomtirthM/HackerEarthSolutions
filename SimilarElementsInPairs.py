def SimilarElementsPairs (A,N):
    #Write your code here
    sorted_list = sorted(A)
    simFlag = False
    res = 0
    count = 0
    prev = sorted_list[0]
    for ele in sorted_list:
        if ele == prev:
            count+=1
        elif prev+1 == ele:
            count+=1
            simFlag = True
        else:
            if simFlag:
                res+=(count * (count - 1)) // 2
                simFlag = False
            count = 1
        prev = ele
    if simFlag:
        res+=(count * (count - 1))//2
    return res

N = int(input())
A = map(int, input().split())
out_ = SimilarElementsPairs(A,N)
print(out_)
