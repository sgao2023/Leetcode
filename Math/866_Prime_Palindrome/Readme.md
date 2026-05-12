https://leetcode.com/problems/prime-palindrome/

# Idea:
Palindromes of even length are divisible by 11. (I got this from the comments of other users.)
So we don't need to consider the palindromes of even length, except for one case: 11. 
That's why I add the following part:
```python
if 8 <= n <= 11:
    return 11
```