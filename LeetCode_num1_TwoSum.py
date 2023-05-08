class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, num in enumerate(nums):
            req = target - num
            if req in check:
                return[check[req], i]
            check[num] = i
        return None
