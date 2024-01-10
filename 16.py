#16.Power Digit Sum
#2 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2 1000?

def find_power(z):
    sum=0
    x=pow(2,z)
    y=str(x)
    for i in y:
        sum=sum+int(i)
    print(sum)

find_power(1000)

#output:1366
