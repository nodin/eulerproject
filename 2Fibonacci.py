def fibItem(n):
    if n<=2:
        #print n, " ",n
        return n
    else:
        resut = fibItem(n-2)+fibItem(n-1)
        #print n, ": ",resut
        return resut

result=0
i=1
while True:
    value = fibItem(i)
    if value>4000000:
        break
    temp = fibItem(i)
    if temp%2 == 0:
        result+=temp
    i+=1
print result
