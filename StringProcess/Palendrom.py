word = input()
length = len(word)
if length == 1:
    print(1)
else :
    for n in range(0, int(length/2) ) :
        if word[n:n+1] != word[length-n-1:length-n] :
            print(0)
            break
        if n == int(length/2)-1 :
            print(1)