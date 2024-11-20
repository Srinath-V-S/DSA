class Solution(object):
    def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """
        binary = ''
        while n>0:
            rem = n%2
            binary = binary + str(rem)
            n = n//2

        return binary.count("1")