from math import sqrt


def isPowerOfThree( n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n = n // 3
    # if a number is pow of 3 then n will be 1 at the end of loop
    return n == 1


def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while n % 4 == 0:
        n = n // 4
    # if a number is pow of 4 then n will be 1 at the end of loop
    return n == 1


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """

    '''
    if n <= 0:
        return False
    while n%2 == 0:
        n = n // 2
    #if a number is pow of 2 then n will be 1 at the end of loop  
    return n==1
    '''
    # NEAT little bitwise solution
    return (n > 0) and (n & (n - 1) == 0)

def main():
    n = 262143



    print(isPowerOfTwo(n))


if __name__=='__main__':
    main()


'''
Bit wise manip soln:
1. Think in terms of binary representation. Key takeway here is binary numbers of pow of 2 numbers always have only one 1.
2.  if subracted from 1 they always return inverted version starting from 1 right to left.
3. Bitwise and of the resultant number and n if zero then it is power of 2



Bitwise AND Truth Table:
Bit A	Bit B	A & B
0	0	0
0	1	0
1	0	0
1	1	1

'''