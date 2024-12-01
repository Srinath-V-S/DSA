import sys

sys.set_int_max_str_digits(10**8)  # Example: Set to a very large number


def fibonacci(n):

    if n <= 1:
        return n
    a,b =0,1
    even_sum = 0
    while b<=n:
        a, b = b, a + b # Move a to b and b to sum(a,b)
        if b % 2 == 0:
            print(b)
            even_sum += b
    return even_sum




print(fibonacci(4000000))