import heapq
#ascending order
def heap_sort_using_min_heap(A):
    # convert the array to Heap
    heapq.heapify(A)  # default to min heap.
    new_list = []

    for i in range(len(A)):
        min_value = heapq.heappop(A)
        new_list.append(min_value)

    # print(new_list)


# descending order
def heap_sort_using_max_heap(B):
    # There is no straight way to use max heap so we can just negate the values during push and re negate when pop operation

    for i in range(len(B)):
        B[i] = -B[i]

    print(B)

    heapq.heapify(B)
    new_list = []

    for i in range(len(B)):
        min_value = -heapq.heappop(B)
        new_list.append(min_value)

    print(new_list)


A = [-3,-2,-4,1,2,5,7,5,3]
heap_sort_using_min_heap(A)
B = [-3,-2,-4,1,2,5,7,5,3]
heap_sort_using_max_heap(B)