class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonfun(prefix,str1):
            i=0
            common=""
            while i<len(prefix):
                if prefix[i]==str1[i]:
                    common+=str1[i]
                else:
                    break
                i+=1
            return common
        
        if len(strs)<=1:
            if len(strs)==0:
                return ""
            return strs[0]
        strs.sort()
        #strs.sort()
        prefix=""

        for c in range(0,len(strs[0])):
            if strs[0][c]== strs[1][c]:
                prefix+=strs[0][c]
            else:
                break
        if len(prefix)==0:
            return ""
        else:
            for i in range(2,len(strs)):
                common=commonfun(prefix,strs[i])
                if len(common)==0:
                    return ""
                else:
                    prefix=common[:]
            return prefix


obj=Solution()
obj.longestCommonPrefix(["flowers","flow","fly"])