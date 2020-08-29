import math

a,b = list(map(int , input().split()))
ok = True
for p in range(a, b+1) :
    if p == 1 :
        ok = True
    elif p == 2 or p == 3 :
        print(p)
    else :
        for k in range(2, int(math.sqrt(p))+1) :
            if p%k == 0 :
                ok = False
                break
                
        if ok == True :
            print(p)
        else :
            ok = True