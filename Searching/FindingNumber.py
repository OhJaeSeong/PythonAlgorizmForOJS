n = int(input())
arrayN = list(map(int , input().split()))
arrayN.sort()
m = int(input())
arrayM = list(map(int , input().split()))
currentPlace = int(0)
searchNum = int(0)
top = len(arrayN)
low = int(0)
center = int((top +  low)/2)
while(currentPlace < m) :
    searchNum = arrayM[currentPlace];
    while True :
        if (top - low) < 5 :
            for j in range(low , top) :
                if arrayN[j] == searchNum :
                    print(1,end='\n')
                    break;
                if j == top-1 :
                    print(0)
            break;
        center = int((top+low)/2)
        if(arrayN[center] == searchNum) :
            print(1)
            break
        elif arrayN[center] >= searchNum :
            top = center
        else :
            low = center
    currentPlace += 1
    top = len(arrayN)
    low = 0
