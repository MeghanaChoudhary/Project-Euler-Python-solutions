#1. Multiples of 3 or 5
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

c1=c2=c3=0
for i in range(1,1000):
    if i%3==0:
        c1+=i
    elif i%5==0:
        c2+=i
    elif(i%15==0):
        c3+=i
print(c1+c2-c3)
