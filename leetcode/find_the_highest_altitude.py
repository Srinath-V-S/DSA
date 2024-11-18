class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        sum = 0
        altitude = [0]
        for i in range(len(gain)):
            sum = sum + gain[i]
            altitude.append(sum)
        return max(altitude)