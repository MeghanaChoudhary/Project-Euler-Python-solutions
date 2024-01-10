#17.Number Letter Counts
#Please let me know how to bug fix this code . I tried and correct a lot of things , but I am 10 extra to the solution !
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def numbers_to_words(n):
    ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if 1<=n<20:
        return ones[n]
    
    elif 20<=n<100:
        return tens[n//10]+ones[n%10]
    elif 100<=n<1000:
        if n%100==0:
            return ones[n//100]+"hundred"
        else:
            return ones[n//100]+"hundredand"+numbers_to_words(n%100)
    elif n==1000:
        return "onethousand"
count=sum(len(numbers_to_words(i)) for i in range(1,1001))
print(count)

#output:21124
