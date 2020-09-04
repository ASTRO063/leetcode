import collections
class Solution:
    def partitionLabels(self, S):
        res=[]
        indexes=collections.OrderedDict()
        for i in range(0,len(S)):
            try:
                if indexes[S[i]]:
                    if len(indexes[S[i]])>1:
                        indexes[S[i]][1]=i
                    else:
                        indexes[S[i]].append(i)
            except:
                indexes[S[i]]=[i]
        temp=list(indexes)
        i=0
        count=0
        extracount=0
        while count<len(S) and i< len(temp) :
            if len(indexes[temp[i]])==1:
                res.append(1)
                count+=1
            else:
                start,end=indexes[temp[i]][0],indexes[temp[i]][1]
                j=i
                flag=0
                for j in range(i+1,len(temp)):
                    if len(indexes[temp[j]]) ==1:
                        if indexes[temp[j]][0]>end:
                            break
                        else:
                            i=j 
                    else:
                        if indexes[temp[j]][0]>end:
                            break
                        else:
                            if indexes[temp[j]][1]>end:
                                i=j
                                extracount=extracount+(indexes[temp[j]][0]-start)
                                end=indexes[temp[j]][1]
                                flag=1
                                break
                            i=j
                if flag==1:
                    continue
                res.append(end-start+1+extracount)
                extracount=0
                count=count+res[-1]
            i=i+1
        return res