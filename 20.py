"""
20.Factorial Digit Sum
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
def factorialRecursive(n):
    if n==0 | n==1:
        return 1
    else:
        product=n*factorialRecursive(n-1)
        return product  
res=factorialRecursive(100)
c=0
string_number=str(res)
for i in string_number:
    c=c+int(i)
print(c)

#output:648
