class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #   for j in range(len(nums)):
        #     if i != j:
        #       if nums[i] == nums [j] and abs(i - j) <= k:
        #         return True
        # Exceeds Time
        
        numDict = {}
        for i, j in enumerate(nums):
          if j in numDict and i - numDict[j] <= k:
            return True
          numDict[j] = i
        return False