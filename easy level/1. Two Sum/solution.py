class Solution:
    def twoSum(self, nums, target):
        dic={}
        for i in range(0,len(nums)):
            if(nums[i] in dic.keys()):
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        for i in range(0,len(nums)):
            rem = target-nums[i]
            if (rem in dic.keys()):
                if(i in dic[rem] and len(dic[rem]) == 1):
                    continue
                if(i in dic[rem] and len(dic[rem]) > 1):
                    return dic[rem]
                else:
                    return [i, dic[rem][0]]


obj=Solution()
nums = [2,7,11,15]
target = 9
obj(nums,target)