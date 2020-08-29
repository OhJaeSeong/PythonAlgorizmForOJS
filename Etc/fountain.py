import sys

num = int(input())
circleNum = 1
direction = False
if num == 1 :
    print("1/1")
else :
    k = num
    loop = 0
    for p in range(2,sys.maxsize) :
        k -= p
        loop += 1
        direction = not(direction)
        if k <= 1 :
            loop -= 1
            k += p
            dirction = not(direction)
            break
    for y in range(loop, loop+1) :
        for x in range(0,y+2) :
            circleNum += 1
            if circleNum == k :
                if direction == False:
                    print((y+2-x),"/",(x+1),sep='')
                    break
                else :
                    print((x+1),"/",(y+2-x),sep='')
                    break
        if k == circleNum :
            break