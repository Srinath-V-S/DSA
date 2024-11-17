def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates_from_sorted_array(nums))


def remove_duplicates_from_sorted_array(nums):
    j = 0
    # [1,1,2]
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]

    return j + 1
if __name__=='__main__':
    main()



'''
two pointers run through
[0,0,1,1,1,2,2,3,3,4]
j  i
[0,1,1,1,1,2,2,3,3,4]
   j i
[0,1,2,1,1,2,2,3,3,4]
     j     i   
[0,1,2,3,1,2,2,3,3,4]
       j       i
[0,1,2,3,4,2,2,3,3,4]
         j          i
loop stops

return j + 1 as j is the index.  
'''