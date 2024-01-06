#10.Summation of Primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_sum(limit):
    s = 0
    for i in range(2, limit):
        if is_prime(i):
            s += i
    print(s)
  
find_sum(2000000)

#output: 142913828922
