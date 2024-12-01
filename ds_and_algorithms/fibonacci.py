def fibonacci(n):

    if n <= 1:
        return n
    a,b =0,1
    print(a)
    print(b)
    for _ in range(2,n+1):
        a, b = b, a + b # Move a to b and b to sum(a,b)
        print(b)
    return b



fibonacci(5)