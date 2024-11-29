'''

Time complexity The average and best-case time complexity is \(O(n\log n)\), while the worst-case time complexity is \(O(n^{2})\)
The average-case space complexity is \(O(\log (n))\), but it can be \(O(n)\) in the worst case.
'''
def quick_sort(A):
    if len(A) <= 1:
        return A

    print(A[:-1])
    pivot = A[-1] # set the pivot as last element of the array
    L = [x for x in A[:-1] if x <= pivot]
    R = [x for x in A[:-1] if x > pivot]

    print(L)
    print(R)

    left = quick_sort(L)
    right = quick_sort(R)


    return left + [pivot] + right




A = [-5,4,2,3,1,7,9,2]
print(quick_sort(A))