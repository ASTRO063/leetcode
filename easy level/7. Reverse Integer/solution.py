class Solution:
    def reverse(self, x) -> :
        a = str(x)
        if a[0] == '-':
            
            x = int('-' + a[-1:0:-1])
            if x >= -2147483648 and x<= 2147483647:
                
                return x
            else:
                return 0
        else:
            x = int(a[::-1])
            if x<= 2147483647:
                
                return x
            else:
                return 0

obj=Solution()
obj.reverse(-1234564)