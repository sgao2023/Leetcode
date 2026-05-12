class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x >= 2
        
        # Construct a palindrome of odd length, 
        # such that its first half is equal to x
        # Example: 
        # 7 -> 7, 35 -> 353, 1234 -> 1234321 
        def make_palindrome(x):
            s = str(x)
            return int(s + (s[:len(s) - 1][::-1]))
        
        if 8 <= n <= 11:
            return 11
        s = str(n)
        if len(s) % 2 == 0:
            curr = 10 ** ((len(s) + 1) // 2)
        else:
            curr = int(s[:len(s)//2 + 1])

        while True:
            x = make_palindrome(curr)
            
            if x >= n and is_prime(x):
                return x
            curr += 1