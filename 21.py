"""
21.Amicable Numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def find_amicable():
    s = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i != j and sum_of_divisors(i) == j and sum_of_divisors(j) == i:
                s = s + i + j
    final_sum = s / 2
    print(final_sum)

def sum_of_divisors(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return s

find_amicable()

#ouput:504
