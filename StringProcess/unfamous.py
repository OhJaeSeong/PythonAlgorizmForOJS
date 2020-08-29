notHearNum, notLookNum = list(map(int,input().split()))
notHears = [str(x) for x in range(0, notHearNum)]
notLooks = [str(x) for x in range(0, notLookNum)]
count = 0
dbj = [str(x) for x in range(0, notHearNum)]
for x in range(0,notHearNum) :
    notHears[x] = str(input())
for y in range(0,notLookNum) :
    notLooks[y] = str(input())
if len(notHears) <= len(notLooks) :
    notHears.sort()
    for p in notLooks :
        top = len(notHears)
        bottom = 0
        center = int((top+bottom)/2)
        while(True) :
           if(top - bottom < 5) :
               for k in range(bottom,top) :
                   if notHears[k] == p :
                       dbj[count] = p
                       count+=1
                       break
               break
           if p > notHears[center] :
               bottom = center
           elif top < bottom:
               break
           elif p == notHears[center]:
               dbj[count] = p
               count+=1
               break
           else :
               top = center

           center = int((top+bottom)/2)
else :
    notLooks.sort()
    for p in notHears :
        top = len(notLooks)
        bottom = 0
        center = int((top+bottom)/2)
        while(True) :
           if(top - bottom < 5) :
               for k in range(bottom,top) :
                   if notLooks[k] == p :
                       dbj[count] = p
                       count+=1
                       break
               break
           if p > notLooks[center] :
               bottom = center
           elif top < bottom:
               break
           elif p == notLooks[center]:
               dbj[count] = p
               count+=1
               break
           else :
               top = center
           center = int((top+bottom)/2)

dbjs = dbj[0:count]
print(count)
dbjs.sort()
for u in range(0,count) :
    print(dbjs[u])