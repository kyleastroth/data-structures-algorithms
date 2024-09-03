class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 1. Initialize a hash table
        hashTable = {}

        # 2. Enumerate through nums
        for idx, num in enumerate(nums):
            # 3. Calculate the complement of the current number
            diff = target - num
            # 4. Check if the difference is present in the hash table
            if diff in hashTable.keys():
                # Return the indices of the two elements if a solution is found
                return [hashTable[diff], idx]
            else:
                # 5. Otherwise, store the current number & index for future reference
                hashTable[num] = idx
        
        return None

        # Time Complexity: O(n) where n is len(nums) because thereis one loop
        # Space Complexity: O(n) since in the worst case each item in nums is inserted into the hash table
