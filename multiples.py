# solution 1
result = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        result+=i
print 'solution 1 %d' %result

# solution 2
global target = 1000
def sumDivisibleBy(n):
    p = target//n
    return n*(p*(p+1))/2

result2 = sumDivisibleBy(3)+sumDivisibleBy(5)-sumDivisibleBy(15)
print 'solution 2 %d' %result2
