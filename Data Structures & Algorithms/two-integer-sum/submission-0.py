class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    if i < j: 
                        return [i, j]
                    else: 
                        return [j, i]
        return output
