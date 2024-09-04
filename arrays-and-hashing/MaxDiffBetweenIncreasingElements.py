class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_diff = -1   # Initialize the max difference as -1 (default if not found)
        min_num = float('inf')  # Initialize the min to infinity to ensure first element we encounter will be smaller than this value

        # Iterate over each number in the list
        for i in nums:
            # If the current num is smaller than the min value we've seen, update the min value
            if i <= min_num:
                min_num = i
            # Otherwise, update the maximum difference 
            else:
                max_diff = max(max_diff, i - min_num)

        return max_diff
