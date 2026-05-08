class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
        # According to the problem's description, any two different nunbers can be canceled. (notice that nums is already sorted)
        # We consider the frequencies of the numbers.
        n = len(nums)
        d = Counter(nums)
        
        
        greatest = max(v for v in d.values())
        if n == greatest:
            return n
        
       
        rest = n - greatest
        if greatest >= rest:
            return greatest - rest
        return n % 2