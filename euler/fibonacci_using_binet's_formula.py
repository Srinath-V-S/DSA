'''

  Fn = {[(√5 + 1)/2] ^ n} / √5


'''
import math

def fibonacci_binet(n):
    phi = (1 + math.sqrt(5))/2


    return round(math.pow(phi,n) / math.sqrt(5))

# Example: Find the 10th Fibonacci number
n = 3
print(f"Fibonacci ({n}) - {fibonacci_binet(n)}")