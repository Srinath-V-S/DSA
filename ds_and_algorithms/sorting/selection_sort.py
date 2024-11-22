'''
Time complexity :O(n^2)
Space complexity : O(1) constant space as we are modifying the array in place.
'''
def selection_sort(A):
    n = len(A)
    for i in range(0,n):
        min_index = i #assume first index is a min index
        for j in range(i+1,n):
            if A[min_index] > A[j]: #if true then there is even smaller value so update min index
                min_index = j
        A[i],A[min_index] = A[min_index], A[i] #once least element is found swap min index value with i value
    return A

A = [6,2,1,5,7]
print(selection_sort(A))