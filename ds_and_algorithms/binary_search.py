def performBinarySearch(arr, target):
    #condition - To perform binary search, base condition is array should be in sorted
    arr_length = len(arr)
    l,r = 0, arr_length - 1
    print(target)
    while l<=r:
        m = (l + r) // 2  # user m = l + (r-l) //2 for big numbers to prevent overflow.
        if arr[m] == target:
            return True
        elif target < arr[m]:
            r = m - 1
        else:
            l = m + 1

    return False

def main():
    arr = [1,1,2,3,5]
    target = 1

    #check whether the input array is in sorted order or not.

    isSorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    if isSorted:
        isTargetFound = performBinarySearch(arr,target)
        if isTargetFound:
            print("Target present in the list")
        else:
            print("Target not present in the list.")
    else:
        print("Input array should be in sorted order")

if __name__=='__main__':
    main()