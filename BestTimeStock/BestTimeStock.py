class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buying = 0
        deposite = 0
        for i in range(len(prices)):
            if (i ==len(prices)-1):
                if buying == 1:
                    buying = 0
                    deposite = deposite+prices[i]
            elif buying == 0 and prices[i] < prices[i+1]:
                buying = 1 
                deposite = deposite - prices[i]
            elif buying ==1 and prices[i]>prices[i+1]:
                buying = 0
                deposite = deposite+prices[i]
        return deposite
