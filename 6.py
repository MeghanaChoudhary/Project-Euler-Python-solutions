#6.Sum Square Difference
#The sum of the squares of the first ten natural numbers is, 12+22+⋯+102=385. The square of the sum of the first ten natural numbers is, (1+2+⋯+10)2=552=3025. 
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640 .
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

c1=0
c2=0
for i in range(1,101):
    c1=c1+(i**2)

for i in range(1,101):
    c2=c2+i
c=c2**2
print(c-c1)

#output: 25164150
