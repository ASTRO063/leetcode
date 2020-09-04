class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=""
        index=0
        ans=0
        while index<len(s):
            #print(substring)
            if s[index] in substring:
                if ans< len(substring):
                    ans=len(substring)
                
                index= index-(len(substring)-1)
                substring=s[index]
            else:
                substring+=s[index]
                # print("index=",index,"string=",substring)
            index=index+1
        if ans< len(substring):
                    ans=len(substring)
        return ans