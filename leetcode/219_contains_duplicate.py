"""
Given an integer array nums and an integer k, return true if there are two distinct 
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict={}
        for i,j  in enumerate(nums):
            if j in dict and abs(i-dict[j])<=k:
                return True
            dict[j]=i
        else:
            return False
        
solution=Solution()
nums = [1,2,3,1]
k = 3
result=solution.containsNearbyDuplicate(nums,k)
print(result)

        
