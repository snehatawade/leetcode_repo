class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        str_num = str(num)

        for ch in str_num:
            if ch!='9':
                a = str_num.replace(ch,'9')
                break
        else:
            a = str_num
        
        for index, ch in enumerate(str_num):
            if index==0 and ch!='1':
                b = str_num.replace(ch,'1')
                break
            elif index>0 and (ch!='0' and ch!='1'):
                b = str_num.replace(ch,'0')
                break
        else:
            b = str_num

        return int(a)-int(b)







        