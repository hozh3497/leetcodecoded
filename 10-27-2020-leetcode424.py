# copied solution, will study when free
# to be updated...
# and need to be optimized.....

from functools import lru_cache
class Solution:
    @lru_cache(None)
    def helper(self, target, mc, mask=None):
        '''
		It can be easily summarized as a minimax problem (we're using a digits DP here for 
		optimization). 
		Here, target -> desiredTarget, mask -> current_state. 
		Since, we can choose an integer (in range 1 to mc) we've used mask as an integer of mc bits,
		which are either set (unused) or unset (used).
		
		The subproblem can be defined as:
		X can win with a particular state (mask) and a target,
		   if for any i from 1 to mc (i not already used), 
		        Y can't win with state(mask - {i}) and (target -i)
		
		Hope you understand with this sloppy explanation, if not please ask :)
		'''
		
        # Base case, if target <= 0, 
        # the match has already ended in the previous state
        if(target <= 0):
            return False
			
        if(mask==None):
            mask = (1 << mc) - 1
        
        res = True
        for i in range(1, mc+1):
            if(((mask >> (i-1)) & 1) == 0):
                continue
			# unsetting the i'th bit using:  mask ^ (1 << (i-1))
            res = res and self.helper(target-i, mc, mask ^ (1 << (i-1)))
        
        return not res
        
        
            
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
	    # Two corner-cases not handled by the helper function
		# 1. If the desiredTotal is already 0, the player is considered the winner, since he can 
		#    use any number and the total becomes more than desired total
        if(desiredTotal == 0): return True
		
		# 2. If the desiredTotal is more than the possible sum using all the numbers from 1 to
		#    maxChoosableInteger, than it is not possible to win anyhow
        if((maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal): return False
        
		# Otherwise
        return self.helper(desiredTotal, maxChoosableInteger)
