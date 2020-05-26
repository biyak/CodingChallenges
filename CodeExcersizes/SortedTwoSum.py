class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for a in range(0, len(numbers)-1):
            if numbers[a] <= target:
                for b in range(a+1, len(numbers)):
                    sum = numbers[a] + numbers[b]
                    if sum == target:
                        return [a+1,b+1]
                    elif sum > target:
                        break
