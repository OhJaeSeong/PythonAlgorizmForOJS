def buildTower(num , fr, by ,to) :
    if num == 1 :
        print(fr,to)
    else :
        buildTower(num-1,fr,to,by)
        print(fr,to)
        buildTower(num-1,by,fr,to)

number = int(input())
sum = pow(2,number)-1
print(sum)
buildTower(number,1,2,3)