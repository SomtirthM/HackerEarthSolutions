def solve(arr):
    start = 0
    end = 0
    res = 0
    for i in s:
        if (i == '('):
            start += 1
        else:
            start -= 1
        if (start < end):
            end = start
            res = 0
        if (end == start):
            res += 1
    if start:
        return 0
    else:
        return res
arr = input()
print(solve(arr))
