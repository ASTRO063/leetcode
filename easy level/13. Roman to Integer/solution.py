class Solution:
    def romanToInt(self, s):
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        res=0
        while len(s)>0:
            try:
                ele=s[0:2]
                if dic[ele]:
                    res+= dic[ele]
                    s=s[2:]
                    
            except:
                res+=dic[s[0]]
                s=s[1:]
        return res      



obj=Solution()
obj.romanToInt("IV")