class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 1. Initialize a hash table
        hashTable = {}

        # 2. Enumerate through nums
        for idx in range(len(nums)):
            # If the number is stored in the hash table, then it is a duplicate
            if nums[idx] in hashTable:
                return True
            # Otherwise, add it to the hash table for future reference
            else:
                hashTable[nums[idx]] = idx

        # 3. If conditions aren't met, no duplicate is found
        return False

        # Time Complexity: O(n) where n is len(nums) because there is one loop
        # Space complexity: O(n) since in the worst case each item in nums is inserted into the hash table

        # Alternative Pythonic Approach: In Python a set removes any duplicates
        # return len(set(nums)) != len(nums)
        # Time & Space Complexity: O(n)
