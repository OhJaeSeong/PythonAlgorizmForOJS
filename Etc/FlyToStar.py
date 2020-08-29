caseNum = int(input())
loop = int(0)
for i in range(0,caseNum) :
    a,b = list(map(int, input().split()))
    if b-a == 1:
        print(1)
    else :
        distance = int(b-a)
        for i in range(1,b-a) :
            distance = distance - i
            loop += 1
            if(distance <= 0) :
                break
            distance = distance - i
            loop += 1
            if(distance <= 0) :
                break
        print(loop)
        loop = int(0)