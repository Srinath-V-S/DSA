class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # same logic as move_zero.py solution only difference is here val is not zero
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        for i in range(j,len(nums)):
            nums[i] = "_"
        return j