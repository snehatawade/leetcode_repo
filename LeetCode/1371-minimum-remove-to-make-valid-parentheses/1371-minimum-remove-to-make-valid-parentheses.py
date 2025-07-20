class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        c=0
        i=0
        while(i<len(s)):
            if s[i]=='(':
                c+=1
                i+=1
            elif s[i]==')':
                c-=1
                if c==-1:
                    s.pop(i)
                    c+=1
                else:
                    i+=1
            else:
                i+=1

        s = s[::-1]
        i = 0
        c = 0
        while(i<len(s)):
            if s[i]==')':
                c+=1
                i+=1
            elif s[i]=='(':
                c-=1
                if c==-1:
                    s.pop(i)
                    c+=1
                else:
                    i+=1
            else:
                i+=1
                

        s = ''.join(s)
        s = ''.join(reversed(s))
        return s
