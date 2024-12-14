# First method is O(n^2) solution, which is easy to figure out.
# Second method is from endless_cheng. Original post:
# https://leetcode.cn/problems/longest-increasing-subsequence/solutions/2147040/jiao-ni-yi-bu-bu-si-kao-dpfu-o1-kong-jia-4zma/
# This is new to me. I should revise this in the future. 
# The further improvement changes nums in-place, which is understandable to me, but hard to memorize. 

# DP O(n^2) solution.
# dp[i] means length of LIS ended with nums[i].
# So, dp[i] = max( {dp[j]+1 | for j satisfies nums[j]<nums[i]})
def lengthOfLIS1(nums: list[int]) -> int:
    dp = [1]*len(nums)
    for i in range(1,len(dp)):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)

# O(n*logn) solution using binary search. 
# This is a bit skillful. 
# g[i] means the minimal possible ending element of IS with fixed length i+1
# We update g when we iterate nums. 
# In every update, use binary search to locate the index in g that need to update.
# For example, nums = [10,9,2,5,3,7,101,18]
# Iterate nums. Initialize g = []
# i=0, g=[10].  g[0]=10 is the minimal possible ending element for IS with length 0+1=1. The corresponding IS is {10}.
# i=1, g=[9]. g[0]=9 is the minimal possible ending element for IS with length 0+1=1. There is no IS with length=2 in nums[:2] so far.
# i=2, g=[2]. g[0]=9 is the minimal possible ending element for IS with length 0+1=1. The corresponding IS is {2}.
# i=3, g=[2,5]. g[1]=5, since so far we have an IS in nums, which is {2,5} ending with 5, and 5 is the minimal possible ending element with length=2.
# i=4, g=[2,3]. Update g[1] as 3. Corresponding IS: {2,3}.
# i=5, g=[2,3,7].
# i=6, g=[2,3,7,101]
# i=7, g=[2,3,7,18]
# In this procedure, notice that:
# (1) Numbers in g are always strictly increasing. (which implies that g consists of unique numbers, no duplicate)
# (2) In every round of iteration, (at most) one element of g will be changed.
# (3) The changement is either substitution of some number of g to nums[i], or append nums[i] to the end of g.
# (4) Therefore, we use binary search to determine where to update or append.

def lengthOfLIS2(nums: list[int]) -> int:
    def lower_bound(arr, target):
        left,right = -1,len(arr)
        while left+1<right:
            mid = left+(right-left)//2
            if arr[mid]>=target:
                right = mid
            else:
                left = mid
        return right
    
    g=[]
    for x in nums:
        index = lower_bound(g,x)
        if index == len(g):
            g.append(x)
        else:
            g[index] = x
    return len(g)

# Improvement: Change nums in-place, instead of creating a new list g.
# We only care about length of g, which is a number. 
# This is called len_g as follows.

def lengthOfLIS3(nums: list[int]) -> int:
    # arr is supposed to be sorted.
    # lower_bound returns the index i (in the range of start<=i<=end) of the first element in arr,
    # such that arr[i]>=target.
    # (Binary search.) 
    def lower_bound(arr, target, start, end):
        left,right = start-1,end+1
        while left+1<right:
            mid = left+(right-left)//2
            if arr[mid]>=target:
                right = mid
            else:
                left = mid
        return right
    # len_g is the index that need to be updated. (corresponds to g.append(nums) in the previous method.)
    len_g = 0
    for x in nums:
        index = lower_bound(nums,x,0,len_g-1)
        print(index,nums)
        if index == len_g:
            len_g += 1
        nums[index] = x
    return len_g

nums = [10,9,2,5,3,7,101,18]
l = lengthOfLIS2(nums)
print(l)
