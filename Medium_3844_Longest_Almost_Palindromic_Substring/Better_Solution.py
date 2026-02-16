class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # returns left, right indices and length of the extended palindrome
        def expand(left: int, right: int) -> tuple:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return (left, right, right - left - 1)
        
        # odd-length palindromes
        for i in range(n):
            l, r = i, i
            l1, r1, length = expand(l, r)
            ans = max(ans, length)
            # skip the left character
            if l1 >= 0:
                ans = max(ans, expand(l1 - 1, r1)[2])
            # skip the right character
            if r1 < n:
                ans = max(ans, expand(l1, r1 + 1)[2])

        # even-length palindromes
        for i in range(n - 1):
            l, r = i, i + 1
            l1, r1, length = expand(l, r)
            ans = max(ans, length)
            # skip the left character
            if l1 >= 0:
                ans = max(ans, expand(l1 - 1, r1)[2])
            # skip the right character
            if r1 < n:
                ans = max(ans, expand(l1, r1 + 1)[2])
        
        return ans