import heapq
#ascending order
def heap_sort_using_min_heap(A):
    # convert the array to Heap
    heapq.heapify(A)  # default to min heap.
    new_list = []
    print(heap_length(A))
    for i in range(len(A)):
        min_value = heapq.heappop(A)
        new_list.append(min_value)

    return new_list


# descending order
def heap_sort_using_max_heap(B):
    # There is no straight way to use max heap so we can just negate the values during push and re negate when pop operation

    for i in range(len(B)):
        B[i] = -B[i]

    heapq.heapify(B)
    new_list = []
    print(heap_length(B))


    for i in range(len(B)):
        min_value = -heapq.heappop(B)
        new_list.append(min_value)

    return new_list

def heap_length(A):
    return len(A)



A = [-3,-2,-4,1,2,5,7,5,3]
print(heap_sort_using_min_heap(A))
B = [-3,-2,-4,1,2,5,7,5,3]
print(heap_sort_using_max_heap(B))

