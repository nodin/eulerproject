"""
      Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
    By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

      By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
    find the sum of the even-valued terms.

"""

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
