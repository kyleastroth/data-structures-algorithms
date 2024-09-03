class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # 1. Initialize a hash table
        hashTable = {}

        # 2. Iterate through strings in array strs
        for s in strs:
            # 3. Sort the string to create a key for the hash table
            sorted_s = ''.join(sorted(s))   # Since sorted returns a list of characters, join them to form a string
            # 4. Add (key, value) pair (sorted_s, s) to hash table
            if sorted_s in hashTable:
                hashTable[sorted_s].append(s)
            else:
                hashTable[sorted_s] = [s]

        # 5. Return the hash table (will already be formatted as a list of lists)
        return hashTable.values()
        
        # Time complexity: Assuming the average len of the strings is n and there are m strings O(m * n log n) because we sort 
        #                  m strings & Python's default sorting algorithm is O(n log n)
        # Space complexity: O(m) since we insert m strings into the dictionary (hashTable)
