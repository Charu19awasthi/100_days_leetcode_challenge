class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        result = []
        digits = "123456789"
        
        for length in range(2, 10):  # numbers with 2 to 9 digits
            for start in range(0, 10 - length):
                num = int(digits[start:start + length])
                
                if low <= num <= high:
                    result.append(num)
        
        return result
        