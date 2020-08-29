sentence = input()
pin = int(0)
answer = int(0)
buho = "+"
k = len(sentence)-1
for i in range(0,len(sentence)) :
    if sentence[i:i+1] == "+" or sentence[i:i+1] == "-" or i == k:
        if buho == "+" :
            if i == k :
                answer += int(sentence[pin:i+1])
            else :
                answer += int(sentence[pin:i])
        else :
           if i == k :
                answer -= int(sentence[pin:i+1])
           else :
                answer -= int(sentence[pin:i])
        pin = i+1
    if sentence[i:i+1] == "-" :
         buho = "-"
print(answer)