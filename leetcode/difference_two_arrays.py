def difference_btw_arrays(nums1, nums2):
    '''

    :param nums1:
    :param nums2:
    :return:
    '''

    '''
    using brute force approach
    list1 = []
    list2 = []
    list3 = []

    for i in range(len(nums1)):
        if nums1[i] not in nums2:
            if nums1[i] not in list1:
                list1.append(nums1[i])
    for i in range(len(nums2)):
        if nums2[i] not in nums1:
                if nums2[i] not in list2:
                    list2.append(nums2[i])
    list3.append(list1)
    list3.append(list2)
    return list3
    '''
    # using sets
    # use set differnce opertion.
    set1, set2 = set(nums1), set(nums2)

    list1 = list(set1 - set2)
    list2 = list(set2 - set1)

    return [list1, list2]

def main():
    nums1 = []

    nums2 = [1,1,2,2]



    print(difference_btw_arrays(nums1,nums2))


if __name__=='__main__':
    main()