class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in range(n):
            gap = target - nums[i]
            if gap in hashmap:
                return [hashmap[gap], i]
            else:
                hashmap[nums[i]] = i