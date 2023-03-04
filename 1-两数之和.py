###哈希
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for ind , val in enumerate(nums):
            if d.get(target - val) is not None:
                return [ind , d[target - val]]
            d[val] = ind