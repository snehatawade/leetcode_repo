class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sx = str(x)
        rev_sx = sx[::-1]
        if sx==rev_sx:
            return True
        else:
            return False
        