class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # 1. Initialize a hash table
        hashTable = {}

        # 2. Initialize a list of lists for Bucket Sort
        freq = [[] for i in range(len(nums) + 1)]

        # 3. Count the frequency of each number
        for n in nums:
            hashTable[n] = 1 + hashTable.get(n, 0) # dictionary.get(key, val) will return specified val if key does not exist

        # 4. Append each (key, value) pair of (num, num_of_occurances) to the appropriate bucket in freq list
        for key, val in hashTable.items():
            freq[val].append(key)
        
        result = []
        # 5. Iterate over freq backwards since occurances are stored in increasing order and add k items to result
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:    # Stop once list has k items
                    return result

        # Time Complexity: O(n) where n is len(nums)
        # Space Complexity: O(n)
