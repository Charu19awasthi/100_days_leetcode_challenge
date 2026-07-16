import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = []
        prefixMax = -inf

        for x in nums:
            prefixMax = max(prefixMax, x)
            mx.append(prefixMax)

        prefix = [gcd(x, y) for x, y in zip(nums, mx)]
        prefix.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left < right:
            ans += gcd(prefix[left], prefix[right])
            left += 1
            right -= 1
        return ans

        