def performTwoSums(nums, target):
    map = {} #HashMap to store each number and its index

    for i in range(len(nums)):
        complement = target - nums[i] #Calculate the complement of the current element
        #Check if the complement is already in the map
        if complement in map:
            return [map[complement],i]
        #Store the current number and its index in the map
        map[nums[i]] = i
    print(map)

def main():
    nums = [2,7,9,11]
    target = 9
    print(performTwoSums(nums,target))




if __name__=='__main__':
    main()