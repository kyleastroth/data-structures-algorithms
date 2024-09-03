class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1. Base Case: if the strings have different lengths they cannot be anagrams
        if len(s) != len(t): return False

        # 2. Initialize a hash table
        hashTable = {}

        # 3. Count the frequency of characters in string s
        for c in s:
            if c in hashTable.keys():
                hashTable[c] += 1
            else: 
                hashTable[c] = 1
        
        # 4. Decrement the frequency of characters in the hash table for each char appearing in string t
        for c in t:
            if c in hashTable.keys():
                hashTable[c] -= 1
            else:
                hashTable[c] = 1
        
        # 5. If any characters in the hash table have a non-zero frequency, the strings cannot be anagrams
        for val in hashTable.values():
            if val != 0: return False
        
        # Otherwise, s & t are anagrams
        return True

        # Time Complexity: O(n), where n is len(s + t)
        # Space Complexity: O(n), where n is len(s) 


        # Alternative Approach: Sorting
        # return sorted(s) == sorted(t)
        # Time Complexity O(n log n) due to the sorting operation where n is the length of the strings
