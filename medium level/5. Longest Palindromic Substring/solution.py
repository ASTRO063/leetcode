class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        if s==s[::-1]:
            return s
        
        substring=""
        res=""
        temp=""
        i=0
        while i< len(s):
            for j in range(i,len(s)):
                temp=s[i:j+1]
                if temp==temp[::-1]:
                    res=temp
            if len(res)>1:
                if len(res)> len(substring):
                    substring=res[:]
                    # s=s[0:i]+s[i+len(res):]
                    # i=i-1
            # print("###",)
            i+=1
        if len(substring)>1:
            return substring
        else:
            return s[0]
            
        