#4.Largest Palindrome Product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

max=0
for i in range(999,99,-1):
    for j in range(i,99,-1):
        p=i*j
        if str(p)==str(p)[::-1]:
            if p>max:
                   max=p
print(max)

# output: 906609
