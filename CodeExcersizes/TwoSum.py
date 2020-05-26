class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(0, len(nums)-1):
            for b in range(a+1, len(nums)):
                if nums[a] + nums[b] == target:
                    return [a,b]
        return -1
