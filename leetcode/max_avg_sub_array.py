class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) == 1:
            return float(nums[0])
        curr_sum = sum(nums[:k])
        max_sum = curr_sum

        '''
        [7,4,5,8,8,3,9,8,7,6]
        1. Calculate the sum upto k intially and store it as curr sum
        2. Loop from k to len(nums) and calculate curr sum in such a way that you lose start(nums[i-k]) of the previous window by subtracting from current sum and add the new element(nums[i]).
        3. find the max sum of the windows.
        4. Finally compute avg.
        '''
        for i in range(k,len(nums)):
            curr_sum +=  nums[i] - nums[i-k]
            max_sum = max(max_sum,curr_sum)
        return max_sum/k