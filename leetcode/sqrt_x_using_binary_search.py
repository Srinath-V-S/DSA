def perfect_square(num):
    x = num ** (1 / 2)
    print('x is ',x)
    return x == int(x)


def main():
    x=5

    print(sqrt_x_binary_search(x))
    print(perfect_square(x))


def sqrt_x_binary_search(x):
    L, R = 1, x

    while L <= R:

        midpoint = (R + L) // 2
        x_squared = midpoint * midpoint

        if x_squared == x:
            return midpoint
        elif x_squared < x:
            L = midpoint + 1
        else:
            R = midpoint - 1
    return R
if __name__ == '__main__':
    main()


"""
idea:

1. Use binary search algorithm to find the sqrt of any number ( since numbers are in sequential order which is the basis for BS)
2. Set lower limit to 1 and upper limit to given input x.
3. As usual find mid point and check the squared value and if it is equal to given number return it.
4. if it is lesser than the given number then increase the lower limit to Midpoint + 1
5. else decrease the Upper limit by midpoint - 1
"""