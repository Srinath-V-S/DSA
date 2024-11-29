def counting_sort(A):
    maxx = max(A)
    count = [0] * (maxx + 1)
    print(count)

    for x in A:
        count[x] +=1

    print(count)

    i = 0
    for c in range(maxx+1):
        while count[c] > 0:
            A[i] = c
            i +=1
            count[c] -=1
    return A


A = [5,2,1,3,6,6,4]

print(counting_sort(A))


#only works for positive numbers.