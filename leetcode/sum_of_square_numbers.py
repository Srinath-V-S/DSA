def sum_of_square_numbers(x):

    if perfect_square(x):
        return True

    for i in range(0,x):
        d = (i**2) + ((i+1)**2)
        if x == d:
            return True

    return False

def perfect_square(num):
    if num == 2:
        return True
    x = num ** (1 / 2)
    return x == int(x)


def main():
    x=8

    print(sum_of_square_numbers(x))

if __name__ == '__main__':
    main()

'''
Problem:

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

idea:
# check if it is a perfect square if it is then return true as it a2 + b2 = c will be true if a is 0 and b is perfect square
# else check till x range if it satisfies the formula


'''