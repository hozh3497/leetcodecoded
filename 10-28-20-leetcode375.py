# solution from web.

import sys
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """
        n = 1 -> min = 0 as there only 1 number to choose
        n = 1 2 -> min = 1 as you guess 1. If it is wrong then it has to be 2
        
        n = 1 2 3. You pick 2, min is 2 as it is lower than it is 1, higher than it is 3
        n = 1 2 3 4. if you pick 3 then min is 4 which is better than 5 if you pick 2 then 3. IMPORTANT: when you pick 3, either it gonna be higher or lower, if higher then it is 4. if lower then it either 1 or 2 which comes back to n = 1 2. Therefore, min is 1 + 3 = 4
        """
        # O(N^2 * N) time as we traverse each pivot for every cell in the matrix | O(N^2) space
        matrix = [[0 for _ in range(n+1)] for i in range (n+1)]
        for Len in range (2,n+1):
            start = 1
            while (start + Len - 1 <= n):
                end = start + (Len - 1) # row:1, col: 3 --> [1,2,3] . Row:2, col 4 --> [2,3,4]
                # finding the minimum cost out of all pivots'cost
                cellMinValue = sys.maxsize
                for pivot in range(start,end + 1): # O(N)
                    cost = pivot
                    left = matrix[start][pivot - 1]
                    right = matrix[pivot+1][end] if pivot+1 <= end else 0
                    cost += max(left,right)
                    # example: [1,2,3,4], we going to take each number as pivot. Here we take 2 as pivot
                    #   cost = 2; minCost of [1] is 0 and minCost of [3,4] is 3. 
                    #   We have to choose 2 + 3 for the worst case
                    cellMinValue = min(cellMinValue,cost) # minimum cost of all pivots'cost
                    
                matrix[start][end] = cellMinValue
                start += 1
        
        return matrix[1][-1]
