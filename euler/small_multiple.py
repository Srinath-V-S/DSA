'''
Mathematically:
LCM(a,b,c)=LCM(LCM(a,b),c)

This property extends to any number of terms:
LCM(a,b,c,d)=LCM(LCM(LCM(a,b),c),d)


LCM Defines the Smallest Common Divisor
The LCM of two numbers is the smallest number divisible by both. Extending this concept, the LCM of 𝑛
 numbers is the smallest number divisible by all n

'''
from math import gcd

n = 20

lcm = 1
for i in range(1,n+1):
    lcm = (lcm * i) // gcd(lcm,i)

print(lcm)


'''
lcm(a,b) = a.b/ gcd(a,b)

lcm(12,18) = 12.18 / gcd(12,18)

gcd(12,18) = 18 mod 12 = 6

12 mod 6 = 0

gcd(12,18) = 6

lcm(12,18) = 12.18/ 6  = 36


'''