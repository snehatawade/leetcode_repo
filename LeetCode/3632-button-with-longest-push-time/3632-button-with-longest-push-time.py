class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        l = len(events)
        a = []
        result = events[0][0] 
        longest = events[0][1]  
        a.append(longest)

        for i in range(1, l):
            n = events[i][1] - events[i - 1][1]
            a.append(n)
            if n > longest:
                longest = n
                result = events[i][0]
            elif n == longest:
                result = min(result, events[i][0])  

        return result
