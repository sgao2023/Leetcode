# My original solution uses DP, 
# which takes O(n*k) time and O(n*k) space,
#  and results in TLE.

# A more efficient way is to apply binary search + DP/greedy approach.

# In the following, my first solution applies binary search.
# The second one was my original DP solution. 

from typing import List

# Binary search + greedy.
# O(n*log m), m=max(nums)-min(nums) Time, 
# O(1) space.
class Solution1:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Iterate nums to get minimum and maximum.
        mx,mn = nums[0],nums[0]
        for x in nums:
            mx = max(mx,x)
            mn = min(mn,x)
        
        # The final answer must be in the range(mn,mx).
        
        # The "check" function checks if we 
        # can find k non-adjacent elements 
        # which are less than or equal to "val".
        
        # The idea here is to steal "as early as possible":
        # Once the thief finds a steal-able house (i.e., value<=val),
        # then grab money from that house.
        def check(val,k):
            i = 0
            cnt = 0
            while i<len(nums) and cnt<=k:
                if nums[i]<=val:
                    cnt += 1
                    if cnt == k:
                        return True
                    # i += 2 due to the non-adjacent restriction.
                    i += 2
                else:
                    i += 1
            return False
        
        # Binary search.
        left,right = mn-1,mx+1
        while left+1<right:
            mid = left + (right-left)//2
            if check(mid,k):
                right = mid
            else:
                left = mid
        return right

# DP solution (TLE).
# O(n*k) time, O(n*k) space.
class Solution2:
    def minCapability(self, nums: List[int], k: int) -> int:
        # dp[i][j] means the min(max value of (j non-adjacent houses from the houses in nums[:i+1]))
        # Core relationship:
        # dp[i][j] = min(steal i-th house, not steal i-th house) = min(max(dp[i-2][j-1],nums[i]),dp[i-1][j])
        # The rest of this code just deals with some boundary conditions.
        dp = [[float('inf')]*(k+1) for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][0] = 0
            for j in range(1,min(i//2+2,k+1)):
                if i>=2:
                    dp[i][j] = min(max(dp[i-2][j-1],nums[i]),dp[i-1][j])
                else:
                    # since j<=i//2+1, i<2, we have j=1
                    dp[i][j] = min(nums[:i+1])

        return dp[len(nums)-1][k]