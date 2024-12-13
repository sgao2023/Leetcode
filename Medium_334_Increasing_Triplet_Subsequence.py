# The follow-up question at the end of the problem asks to solve it with O(n) time complexity and O(1) space complexity.
# The following 2nd method fits this requirement.

# Two methods. The first method uses prefix minimum and suffix maximum, which takes O(n) extra space.
# The second method is a bit skillful. The idea is from 'medium 300: Longest Increasing Subsequence'(LIS).

def increasingTriplet(nums: list[int]) -> bool:
    pre_min = [0]*len(nums)
    suf_max = [0]*len(nums)
    for i in range(len(nums)):
        if i==0:
            pre_min[i] = nums[0]
            continue
        pre_min[i] = min(nums[i],pre_min[i-1])
    for i in range(len(nums)-1,-1,-1):
        if i == len(nums)-1:
            suf_max[i] = nums[i]
            continue
        suf_max[i] = max(nums[i],suf_max[i+1])
    for i in range(1,len(nums)-1):
        if nums[i]>pre_min[i-1] and nums[i]<suf_max[i+1]:
            return True
    return False

def increasingTriplet1(nums: list[int]) -> bool:
    suf_max = [0]*len(nums)
    # for i in range(len(nums)):
    #     if i==0:
    #         pre_min[i] = nums[0]
    #         continue
    #     pre_min[i] = min(nums[i],pre_min[i-1])
    for i in range(len(nums)-1,-1,-1):
        if i == len(nums)-1:
            suf_max[i] = nums[i]
            continue
        suf_max[i] = max(nums[i],suf_max[i+1])
    pre_min = nums[0]
    for i in range(1,len(nums)-1):
        pre_min = min(nums[i-1],pre_min)
        if nums[i]>pre_min and nums[i]<suf_max[i+1]:
            return True
    return False
        

# The idea is from 'medium 300: Longest Increasing Subsequence'(LIS).
# There is a way to solve LIS problem with O(n*logn) time complexity. 
# Here since we only need to find an increasing sequence with length>=3, so the length of g is at most 3. 
# Therefore, its time complexity is O(n*log3)~O(1).
# Reference:
# https://leetcode.cn/problems/longest-increasing-subsequence/solutions/2147040/jiao-ni-yi-bu-bu-si-kao-dpfu-o1-kong-jia-4zma/
def increasingTriplet2(nums: list[int]) -> bool:
    def lower_bound(arr,target):
        left,right = -1,len(arr)
        while left+1<right:
            mid = left+(right-left)//2
            if arr[mid]>=target:
                right = mid
            else:
                left = mid
        return right
    i=0
    g=[]
    while i<len(nums):
        x = nums[i]
        ind = lower_bound(g,x)
        if ind==len(g):
            g.append(x)
        else:
            g[ind] = x
        if len(g)>=3:
            return True
        i+=1
    
    return False

nums_list = [[1,2,3,4,5],[5,4,3,2,1],[2,1,5,0,4,6]]
for nums in nums_list:
    print(increasingTriplet(nums),increasingTriplet1(nums),increasingTriplet2(nums))
