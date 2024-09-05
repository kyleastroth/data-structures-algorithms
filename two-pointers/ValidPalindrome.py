class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        left = 0
        right = len(s) - 1

        while right >= len(s)/2:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
