class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:          
        hour,mintue=0,0
        flag=False
        a,b=0,0
        time={}
        for i in range(0,4):
            for j in range(0,4):
                temp=(A[i]*10 + A[j])   
                if i!=j and temp>=0 and temp<=23 :
                    hour=A[i]*10 + A[j]
                    i1,i2=i,j
                    a,b=A[i1],A[i2]
                    A[i1],A[i2]=None,None
                    mintues=[A[k] for k in range(0,4) if A[k]!=None ]
                    flag=True
                    if mintues[0]>=mintues[1]:
                        mintue= str(mintues[0]) + str(mintues[1])
                    else:
                        mintue= str(mintues[1]) + str(mintues[0])
        
                    if int(mintue) >=60:
                        mintue=mintue[::-1]
                        if int(mintue)>=60:
                            flag=False
                    if flag==True:
                        time[hour]=mintue
                    A[i1],A[i2]=a,b
                        
        if len(time) ==0:
            return ""
        else:
            hour=max(time.keys())
            mintue=time[hour]
            return str(hour//10)+str(hour%10)+":"+str(mintue)
        
                