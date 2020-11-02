# based on solution found on web. A nice dp excercise.

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        #memo = {}
        Len = len(piles)
        
        def find(i,k):
            if i+2*k>=Len:
                return acc[i]
            return acc[i]-min(find(i+x,max(x,k)) for x in range(1,2*k+1))

        acc=[]
        s=0
        for i in range(Len-1,-1,-1):
            s+=piles[i]
            acc.append(s)
        acc=acc[::-1]
        return(find(0,1))


        
#         def helper(i,j):
#             if i>=Len:
#                 return 0
#             if (i,j) in memo:
#                 return memo[(i,j)]
#             Max = float("-inf")
            
#             for c in range(1, 2*i + 1):
#                 j = j + c
#                 if totalL > Len:
#                     break
#                 i = max(j, c)
#                 curt = sum(piles[j: totalL])
#                 Max = max(Max, curt - helper(i, j))
