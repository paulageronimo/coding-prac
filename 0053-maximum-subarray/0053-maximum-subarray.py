class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = maxArr =nums[0]
        
        for num in nums[1:]:
          arr = max(num, arr+num)
          maxArr = max(maxArr, arr)
        
        return maxArr