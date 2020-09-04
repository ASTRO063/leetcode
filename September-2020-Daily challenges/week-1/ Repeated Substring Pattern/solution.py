class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        st=s[0]
        half=len(s)//2
        for i in range(0,half):    
            # print("sub",st)
            # if len(st)%2 ==0:
            #     pass
            # else:
            #     pass
            rst=st[:]
            while len(rst) < len(s):
                rst=rst+st
            # print("str",rst)
            if rst==s:
                return True
            else:
                st=s[:i+2]
                # print("edsd==",st)
        return False