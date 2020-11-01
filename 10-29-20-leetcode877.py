class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # apparently, there is only one possible winner, always....
        # return True
        
        # the dp solution
        
#         N = len(piles)
        
#         def helper(i,j):
#             if i>j:
#                 return 0
#             turn = (j-i-N)%2
#             if turn==1:
#                 return max(piles[i]+helper(i+1,j),piles[j]+helper(i,j-1))
#             else:
#                 return min(-piles[i]+helper(i+1,j),-piles[j]+helper(i,j-1))
            
#         return helper(0,N-1) > 0

        def find(array,memo,i,j):
            if(i,j) in memo:
                return memo[i,j]
            if i>j:
                return 0
            score_A=array[i]+min(find(array,memo,i+1,j-1),find(array,memo,i+2,j))
            score_B=array[j]+min(find(array,memo,i,j-2),find(array,memo,i+1,j-1))
            my_score=max(score_A,score_B)
            memo[i,j]=my_score
            return my_score

        memo = {}
        i=0
        j=len(piles)-1
        
        score=find(piles,memo,i,j)
        total=sum(piles)
        return score>=total-score

