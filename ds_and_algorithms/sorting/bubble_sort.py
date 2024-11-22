

'''
Time complexity :
 O(n^2) very slow Worst case if input array is in  reverse order
 O(n) for best case when arr is already in sorted order.
Space complexity : O(1) constant space as we are modifying the array in place.
'''
def bubble_sort(A):
    n = len(A)
    for j in range(0,n):
        swap = False
        for i in range(1,n-j):
            if A[i] < A[i-1]:
                A[i],A[i-1] = A[i-1],A[i]
                swap = True
        if not swap:
            break

    return A

A = [6,2,1,5,7]
print(bubble_sort(A))