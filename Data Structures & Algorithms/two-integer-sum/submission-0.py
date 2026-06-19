class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in seen:
                return [seen[val], i]
            seen[nums[i]] = i
        return None