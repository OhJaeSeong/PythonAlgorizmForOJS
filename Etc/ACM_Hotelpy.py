caseNumber = int(input())
for c in range(0,caseNumber) :
    h,w,n = list(map(int, input().split()))
    place = int(101)
    people = int(1)
    for ww in range(0,w) :
        for hh in range(0,h) :
            if people == n :
                print(place)
                break
            elif hh == h-1 :
                continue
            else :
                people += 1
                place += 100
        if people == n :
            break
        else :
            place = place - 100*(h-1) + 1
            people += 1
