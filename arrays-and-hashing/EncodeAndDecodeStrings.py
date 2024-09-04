class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """

        encoded_string = [] # Initialize an empty list to store strings in format 'num_chars:str'

        for s in strs:
            encoded_string.append('%d:' % len(s) + s)   # Add each 'num_chars:str' string to list

        return ''.join(encoded_string)  # Join list into single string

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        
        decoded_strings = []    
        i = 0

        while i < len(s):
            colon_idx = s.find(':', i)  # string.find(value, start, end) returns index of first occurance
            i = colon_idx + 1 + int(s[i:colon_idx]) # i = index at end of word 
            decoded_strings.append(s[(colon_idx + 1):i])

        return decoded_strings

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
