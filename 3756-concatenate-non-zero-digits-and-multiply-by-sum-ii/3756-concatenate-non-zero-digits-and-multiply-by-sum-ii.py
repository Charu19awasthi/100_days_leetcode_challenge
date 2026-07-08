class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # Prefixes for building X and calculating digit sums
        pref_x = [0] * (n + 1)
        pref_sum = [0] * (n + 1)
        pref_count = [0] * (n + 1)  # Tracks the number of non-zero digits
        
        # Precompute powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        for i, char in enumerate(s):
            digit = ord(char) - ord('0')
            if digit != 0:
                pref_x[i + 1] = (pref_x[i] * 10 + digit) % MOD
                pref_sum[i + 1] = pref_sum[i] + digit
                pref_count[i + 1] = pref_count[i] + 1
            else:
                pref_x[i + 1] = pref_x[i]
                pref_sum[i + 1] = pref_sum[i]
                pref_count[i + 1] = pref_count[i]
                
        results = []
        for l, r in queries:
            count_nonzero = pref_count[r + 1] - pref_count[l]
            if count_nonzero == 0:
                results.append(0)
                continue
                
            # Extract x % MOD using prefix math
            x_mod = (pref_x[r + 1] - pref_x[l] * pow10[count_nonzero]) % MOD
            digit_sum = pref_sum[r + 1] - pref_sum[l]
            
            results.append((x_mod * digit_sum) % MOD)
            
        return results