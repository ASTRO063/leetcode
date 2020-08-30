class Solution:
    def isPalindrome(self, x) :
        if x<0:
            return False
        num=str(x)
        re_num=num[::-1]
        if num==re_num:
            return True
        else:
            return False


obj=Solution()
abj.isPalindrome(-212)