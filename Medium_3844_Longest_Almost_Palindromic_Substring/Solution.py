class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        ans = 0
        # odd-length palindromes
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, r - l - 1)

            # try to expand the palindrome by skipping one character
            l1, r1 = l, r
            # skipping the left character
            if l1 >= 0:
                l =  l1 - 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, r - l - 1)
            # skipping the right character
            if r1 < n:
                r = r1 + 1
                l = l1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, r - l - 1)

        # even-length palindromes
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, r - l - 1)

            # try to expand the palindrome by skipping one character
            l1, r1 = l, r
            # skipping the left character
            if l1 >= 0:
                l =  l1 - 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, r - l - 1)
            # skipping the right character
            if r1 < n:
                r = r1 + 1
                l = l1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            ans = max(ans, r - l - 1)
        
        return ans