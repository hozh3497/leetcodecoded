class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(i,j, memo):
            # place two pointers to simulate the process of selecting numbers
            # if the first element is selected, then i advances by 1
            # otherwise j goes backwards by 1
            if i==j:
                return nums[i]
            # only keep track of the difference at each turn, and see if the maximum possible difference is greater than 0 (if it is, then player 1 can be the winner).
            # within the max function: (left) player 1 picks the front;
            # (right) player 1 picks the end.
            if (i,j) in memo:
                return memo[(i,j)]
            mval = max(nums[i]-helper(i+1,j,memo),nums[j]-helper(i,j-1,memo))
            memo[(i,j)] = mval
            return mval
        
        memo = {}
        maxVal = helper(0,len(nums)-1,memo)
        
        if maxVal>=0:
            return True
        return False
        
