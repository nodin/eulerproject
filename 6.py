square_sum=0
sum=0
for i in range(1,101):
    square_sum=i**2+square_sum
    sum=sum+i
print sum**2 - square_sum
