from typing import List
from collections import defaultdict
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:

        def count_substrings(s,window_length,count):
            
            n_alphabets = window_length//count
            left = ans = 0
            d = defaultdict(int)
            for right,ch in enumerate(s):
                d[ch] += 1
                while d[ch] > count:
                    d[s[left]] -= 1
                    if d[s[left]] == 0:
                        del d[s[left]]
                    left += 1
                if right-left+1<window_length:
                    continue
                while len(d)>n_alphabets:
                    d[s[left]] -= 1
                    if d[s[left]] == 0:
                        del d[s[left]]
                    left += 1
                if right-left+1 == window_length:
                    ans += 1

            return ans
        
        ans = 0
        for number_of_unique_alphabets in range(1,27):
            ans += count_substrings(s,number_of_unique_alphabets*count,count)
        return ans

s = 'ax'
sol = Solution()

a = sol.equalCountSubstrings(s,1)
print(a)