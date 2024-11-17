def applyOperations(nums):
    j = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i] * 2
            nums[i + 1] = 0

    #Transposing into move zero problem using 2 pointer.
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j+=1
            print(nums)

    for i in range(j,len(nums)):
        nums[i] = 0



def main():
    nums = [1,2,2,1,1,0]


    applyOperations(nums)


if __name__=='__main__':
    main()


'''

[1,2,2,1,1,0]
            

'''