#5.Smallest Multiple
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?

found = False
n = 1
factors = range(1, 21)
while not found:
    found = True
    for x in factors:
        if n % x != 0:
            found = False
    if found:
        print(n)
    n=n+1
