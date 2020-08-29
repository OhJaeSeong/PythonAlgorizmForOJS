n = int(input())
nCount = [int(x) for x in range(0,n+1)]
if n == 0 :
    nCount[0] = 0
else :
    nCount[0] = 1
    nCount[1] = 1
    if n > 1 :
        for k in range(2,n+1) :
            nCount[k] = nCount[k-2] + nCount[k-1]
            nCount[k] = nCount[k]%15746
print(nCount[n])