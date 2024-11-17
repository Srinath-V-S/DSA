def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num - 2)



def main():

    # Fibonacci series idea => F(n) = F(n-1) + F(n-2)
    print(fibonacci(3))




if __name__ == '__main__':
    main()