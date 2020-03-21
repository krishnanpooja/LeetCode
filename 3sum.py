'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.


'''



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        soln = []
        length = len(nums)
        for i in range(length):
            for j in range(length-1,0,-1):
                if i!=j:
                    val = -(nums[i]+nums[j])
                    if val in nums:
                        if (nums.index(val)!=i and nums.index(val)!=j):
                            res = [nums[i],nums[j],-(nums[i]+nums[j])]
                            soln.append(res)
        result = list(set(tuple(sorted(sub)) for sub in soln)) 
        return result
