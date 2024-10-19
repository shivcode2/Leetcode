class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # This dict contains {numbers : index}
      complimentMap = {}
        for i in range(len(nums)):
            compliment_num = target - nums[i]
            # If the complement number is found in the dict, then return "current number's index" and "complement number's index"
            if compliment_num in complimentMap:
                return [i, complimentMap[compliment_num]]
            complimentMap[nums[i]] = i
        return []
