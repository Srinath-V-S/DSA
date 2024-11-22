'''
Time complexity :
 O(n^2) very slow Worst case - Every element must be compared with all previous elements
 O(n) for best case (Already sorted) if inner loop terminates immediately
Space complexity : O(1) constant space as we are modifying the array in place.
'''
def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        # loop moves backwards to put A[i] in the correct sorted position
        for j in range(i,0,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
            else:
                break

    return A

A = [6,2,1,5,7]
print(insertion_sort(A))