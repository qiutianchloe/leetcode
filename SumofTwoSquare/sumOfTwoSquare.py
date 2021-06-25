import math 
class Solution(object):
    def judgeSquareSum(self, c):
        if c == 0 or c==1 : return True
        if c % 4 == 3: return False
        
        m = int(math.sqrt(c))
        for a in range(1, m + 1):
            b = c - a * a
            if int(math.sqrt(b)) ** 2 == b:
                return True
        return False

ob = Solution()
ob.judgeSquareSum(3) 
print("for number 3, there are two interge a, b such that a*a+b*b = 3")
print(ob.judgeSquareSum(3))
print("for number 5, there are two interge a, b such that a*a+b*b = 5")
print(ob.judgeSquareSum(5))
