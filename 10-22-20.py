# leetcode 494--target sum

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # at each step, there are two options:
        # inserting either a plus or a minus sign
        # keep the results that sum up to the target
        # can do this through recursion.
        # can be optimized via memoization
        count = 0
        memo = {}
        
        def helper(idx, nums, curSum, memo):
            # base case
            if (curSum, idx) in memo:
                return memo[(curSum, idx)]
            
            if curSum==S:
                if idx==len(nums):
                    return 1
            elif idx>=len(nums):
                return 0
            
            # total count + counts from idx, either adding the next or subtracting the next integer. Keep track of the count from the current idx with current sum.
            count = helper(idx+1, nums, curSum+nums[idx], memo)+helper(idx+1, nums, curSum-nums[idx], memo)
            memo[(curSum,idx)] = count
            
            return count
        
        return helper(0, nums, 0, memo)
