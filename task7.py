n = int(input())
if n == 1:
    print('None')
else:
    res = []
    for i in range(2, n + 1):
        is_prs = 1
        for j in res:
            if i % j == 0:
                is_prs = 0
                break
        if is_prs == 1:
            res.append(i)
        is_prs = 1
    print(*res)