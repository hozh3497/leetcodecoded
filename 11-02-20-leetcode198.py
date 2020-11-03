class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if not nums:
            return 0
        
        if L==1:
            return nums[0]
        total = [0]*L
        total[0] = nums[0]
        total[1] = max(nums[0],nums[1])
        
        for i in range(2,L):
            total[i] = max(total[i-2]+nums[i],total[i-1])
            
        return total[-1]
