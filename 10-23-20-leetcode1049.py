# will try to add other solutions when I have more time.

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Considering the information provided in hints, the problem can be translated as finding the combination of + and - signs in front of elements in the array such that the final sum is minimized.
        # This further boils down to the problem of finding the minimum difference between two subarrays of the initial array. So:
        # At the split of the array, we want to find min(subarr1-subarr2)
        # This can be rewritten as min(subarr1+subarr2-2*subarr2)
        # Then we need to find the subarr2 that achieves the max sum without exceeding the constraint: 2*subarr2<=sum_arr (since the sum is bounded by 0)
        # We can sort of search through the sum of subarrays then.
        
        totalSum = sum(stones)
        memo = [0]*(totalSum//2+1) # use a list to keep track of the stone weight at each potential partition point
        
        for i in range(len(stones)):
            for s in range(totalSum//2):
                smax = totalSum//2-s
                if smax>=stones[i]:
                    memo[smax] = max(memo[smax],memo[smax-stones[i]]+stones[i])
                    
        minWeight = totalSum - 2*memo[totalSum//2]
        return minWeight
