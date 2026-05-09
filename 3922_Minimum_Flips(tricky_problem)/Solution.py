class Solution:
    def minFlips(self, s: str) -> int:
        if len(s) < 3:
            return 0
        n = len(s)
        d = Counter(s)
        c0, c1 = d['0'], d['1']
        if c1 == 1 or c0 == 0 or c1 == 0 or (c1 == 2 and s[0] == '1' and s[-1] == '1'):
            return 0
        # Set all elements to "0"
        res1 = c1
        # Set all elements to "1"
        res2 = c0
        # Set all elements but one to "0"
        res3 = c1 - 1
        # Set the first and the last to "1", and all others to "0" 
        res4 = 0
        if s[0] == '0':
            c0 -= 1
            c1 += 1
            res4 += 1
        if s[-1] =='0':
            c0 -= 1
            c1 += 1
            res4 += 1
        # Minus 2 from c1, because the first and last are "1". 
        res4 += (c1 - 2)
        return min(res1, res2, res3, res4)