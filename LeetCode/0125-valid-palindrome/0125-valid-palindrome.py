class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower().strip().replace(" ", "")
        s = ''.join(c for c in s if c.isalnum())
        revS = s[::-1]
        print(revS)
        if revS==s:
            return True
        else:
            return False





        