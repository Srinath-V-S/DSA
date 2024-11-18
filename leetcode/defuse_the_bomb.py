def main():
    code = [2,4,9,3]
    k = -2
    result = decrypt(code,k)
    print(result)

def decrypt(code, k):
    n = len(code)
    result = []
    for i in range(n):
        sum = 0
        if k == 0:
            return [0] * len(code)
        elif k > 0:
            for j in range(1, k + 1):
               sum += code[(i + j) % n]
        else:
            for j in range(1, -k + 1):
               sum += code[(i-j) % n]
        result.append(sum)

    return result
if __name__ == '__main__':
    main()


'''
Key takeways when dealing with cyclic arrays
1.Use modulo operation to circle back the array
2. Use [-1] negative indices to get previous element starting from 0 (rotation)
'''