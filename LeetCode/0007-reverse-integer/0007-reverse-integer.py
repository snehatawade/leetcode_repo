class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1 
        else:
            sign = 1
        x = abs(x)
        reversed_x = int(str(x)[::-1]) * sign
        
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        return reversed_x



        