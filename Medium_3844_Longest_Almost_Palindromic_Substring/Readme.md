# Center Expansion

### Time complexity: O(n^2)
### Space complexity: O(1)

1. Enumerate every possible center and extend the palindrome around the center.

2. When a mismatch happens, try to skip the left index or the right index, and continue expanding. 

3. Handle odd- and even-length palindromes separately. For odd-len palindromes, the code is like 
```
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
```

For even-len palindromes, we have 
```
    for i in range(n - 1):
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
```

4. We can also unify the odd-len part and even-len part, that's a bit technical. 

5. Solution.py is my initial implementation. I improved my code in Better_Solution.py by using a helper function.