class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            # print("index1=",len(nums1)//2,"index2=",(len(nums1)//2)-1)
            # print("value1=",nums1[len(nums1)//2])
            # print("value2=",nums1[(len(nums1)//2)-1])
            # print("median=",(nums1[len(nums1)//2] +nums1[(len(nums1)//2)-1])/2)
            return (nums1[len(nums1)//2] +nums1[(len(nums1)//2)-1])/2
        else:
            # print("index=",len(nums1)//2)
            # print("median=",nums1[len(nums1)//2])
            return float(nums1[len(nums1)//2])