import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum=[]
        odd_sum=[]
        for i in range(1,(n*2)+1):
            if i % 2==0:
                even_sum.append(i)
            else:
                odd_sum.append(i)

        esum=sum(even_sum)
        osum=sum(odd_sum)

        return(math.gcd(esum,osum))


        