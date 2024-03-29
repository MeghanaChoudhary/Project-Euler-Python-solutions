#9.Special Pythagorean Triplet
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,a^2 + b^2 = c^2 For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the product abc.

for a in range(1,1001):
    for b in range(1,1001):
        c=1000-a-b
        if c<0:
            break
        if a*a+b*b==c*c:
            print(a*b*c)

#output: 31875000
