def getMax(a,b):
    if(a > b):
        return a
    else :
        return b
num = input()
num = int(num)
wine = [int(k) for k in range(num+1)]
maxWine = [int(k) for k in range(num+1)]
wine[0] = 0
maxWine[0] = 0;
for n in range(1 , num+1 ):
    wine[n] = int(input())
maxWine[1] = int(wine[1])
if(int(num) > 1):
    maxWine[2] = wine[1]+wine[2]
if(int(num) > 2):
    for n in range(3,num+1):
        maxWine[n] = getMax(int(maxWine[n-3])+int(wine[n])+int(wine[n-1]),
                           int(maxWine[n-2]) + int(wine[n]))
        maxWine[n] = getMax(int(maxWine[n-1]), int(maxWine[n]))
print(maxWine[num])