height = int(0)
stars = [[]]
def StarLink(sqrt , isBlank, x, y) :
    if isBlank :
        for p in range(y,y+sqrt) :
            for t in (x,x+sqrt) :
                stars[y][x] = ' '
        return;

    if sqrt == 1 :
        stars[y][x] = '*'
        return;

    searchBlank = int(0)
    for i in range(y,y+sqrt,int(sqrt/3)) :
        for j in range(x,x+sqrt,int(sqrt/3)) :
            searchBlank += 1
            if searchBlank == 5 :
                StarLink(int(sqrt/3),True,j,i)
            else :
                StarLink(int(sqrt/3),False,j,i)
       
threeSqrt = int(input())
height = threeSqrt
stars = [ [ ' ' for x in range(threeSqrt)] for y in range(threeSqrt)]
StarLink(threeSqrt,False, 0,0)
for s in range(0,threeSqrt) :
    for k in range(0,threeSqrt) :
        print(stars[s][k],end='')
    print()