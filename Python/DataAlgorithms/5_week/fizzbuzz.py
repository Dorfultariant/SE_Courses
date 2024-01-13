for k in input().split(sep=' '):
    word=""
    if int(k)%3==0:word+="Fizz"
    if int(k)%5==0:word+="Buzz"
    if word!="":print(word)