def main():
    nums = [0,1,0,3,12]
    move_zero(nums)


def move_zero(nums):
    j = 0
    # find how many non zero numbers are there
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j+=1
    # using j fill the remaining values as zero
    for i in range(j,len(nums)):
        nums[i] = 0

    print(nums)
if __name__ == '__main__':
    main()