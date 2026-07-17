import math
import bisect

class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for x in nums:
            freq[x] += 1

      
        cnt = [0] * (max_val + 1)
        for g in range(1, max_val+1):
            for multiple in range(g, max_val+1, g):
                cnt[g] += freq[multiple]

        exact = [0] * (max_val + 1)
        for g in range(max_val, 0, -1):
            total = cnt[g] * (cnt[g]-1) // 2
            for multiple in range(2*g, max_val+1, g):
                total -= exact[multiple]
            exact[g] = total

   
        gcds = []
        counts = []
        running = 0
        for g in range(1, max_val+1):
            if exact[g] > 0:
                running += exact[g]
                gcds.append(g)
                counts.append(running)

        
        ans = []
        for q in queries:
            idx = bisect.bisect_right(counts, q)
            ans.append(gcds[idx])
        return ans
