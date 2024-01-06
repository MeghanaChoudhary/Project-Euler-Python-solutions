#7. 10001st prime number
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    p = []
    num = 2
    while len(p) < n:
        if is_prime(num):
            p.append(num)
        num += 1
    return p[-1]

result = nth_prime(10001)
print(result)

#output:104743
