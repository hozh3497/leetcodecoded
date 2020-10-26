'''
commented section needs debugging. Working code from web.
'''

class Solution:
#     def splitArraySameAverage(self, A: List[int]) -> bool:
#         # create two empty list B and C
#         # the average of B and C is the same as the average of A
#         target = sum(A)/2
        
#         # Then we can basically iterate through the array and ask
#         # whether we should add the element to the subarray
#         # If we reached the target, then check if the remaining elements
#         # in A sum up to target.
#         # If they do, then there is an answer. Otherwise it's not possible with
#         # the current combination.
        
#         memo = {}
        
#         def helper(target, i, memo, k, s, k0):
#             # base case: s (the running sum) reaches target
#             # k: keeps track of how many elements are put in B
#             # checking all possible k from the smallest to largest
            
#             if k==0:
#                 if s/k0==target/(len(A)-k0):
#                     print(s,i,k)
#                     return True
#                 return False
            
#             if k+i>len(A):
#                 return False
            
#             if (k,s,i) in memo:
#                 return memo[(k,s,i)]
            
#             #print(i,k)
            
#             memo[(k-1,s+A[i],i+1)] = helper(target,i+1,memo,k-1,s+A[i],k0) or helper(target,i+1,memo,k,s,k0)
#             #print(memo)
#             return memo[(k-1,s+A[i],i+1)]
            
#         for j in range(1,len(A)//2+1):
#             print(helper(target,0,memo,j,0,j))
#             if helper(target,0,memo,j,0,j) is True:
#                 return True
#         return False
    def splitArraySameAverage(self, A: List[int]) -> bool:
        mem = {}

        def find(target, k, i):
            if k == 0: return target == 0
            if k + i > len(A): return False
            if (target, k, i) in mem: return mem[(target, k, i)]
            mem[(target - A[i], k - 1, i + 1)] = find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)
            return mem[(target - A[i], k - 1, i + 1)]

        n, s = len(A), sum(A)
		

        return any(find(s * j // n, j, 0) for j in range(1, n // 2 + 1) if s * j % n == 0)
        
        
