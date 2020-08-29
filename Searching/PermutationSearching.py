sum , leastNum = list(map(int , input().split()))
if leastNum > 100 :
    print(-1)
else :
    for i in range(leastNum,101) :
        s = (sum - int(((i-1)*i)/2))/i
        if i%2 == 1 and sum%i == 0 :
            if(int(sum/i)-int(i/2) >= 0) and i+1 <= 100:
                 for k in range(int(sum/i)-int(i/2) , int(sum/i)+int(i/2)+1 ) :
                    print(k, end=' ')
                 break
        elif i%2 == 0 and sum%i == i/2 :
            if int(sum/i)-int(i/2)+1 >= 0 and i <= 100:
                for p in range(int(sum/i)-int(i/2)+1, int(sum/i)+int(i/2)+1) :
                    print(p, end=' ')
                break
        elif i == 100 :
            print(-1)
'''백준 1024 수열의 합'''