class Solution:
    def longestBalanced(self, s: str) -> int:

        def cnt_1_letter(ch):
            ans = 0
            i = 0
            start = 0
            while i < len(s):
                if s[i] != ch:
                    start = i + 1
                    cnt = 0
                    i += 1
                    continue
                ans = max(ans, i - start + 1)
                i += 1

            return ans

        def cnt_2_letters(ch1, ch2, ch_skip):
            ans = 0
            i = 0
            pre = {(0, 0): i}
            cnt1 = cnt2 = 0
            while i < len(s):
                if s[i] == ch_skip:
                    pre = {(0, 0): i + 1}
                    cnt1 = cnt2 = 0
                    i += 1
                    continue
                if s[i] == ch1:
                    cnt1 += 1
                elif s[i] == ch2:
                    cnt2 += 1

                if (0, cnt2 - cnt1) in pre:
                    left = pre[(0, cnt2 - cnt1)]
                    ans = max(ans, i - left + 1)

                if (0, cnt2 - cnt1) not in pre:
                    pre[(0, cnt2 - cnt1)] = i + 1

                i += 1

            return ans

        def cnt_3_letters(ch1, ch2, ch3):
            pre = {(0, 0, 0): 0}
            ans = cnt1 = cnt2 = cnt3 = 0
            for i, ch in enumerate(s):
                if ch == ch1:
                    cnt1 += 1
                elif ch == ch2:
                    cnt2 += 1
                elif ch == ch3:
                    cnt3 += 1
                if (0, cnt2 - cnt1, cnt3 - cnt1) in pre:
                    left = pre[(0, cnt2 - cnt1, cnt3 - cnt1)]
                    ans = max(ans, i - left + 1)
                else:
                    pre[(0, cnt2 - cnt1, cnt3 - cnt1)] = i + 1
            return ans

        res1 = 0
        # Count substrings containing only one kind of characters.
        for ch in ["a", "b", "c"]:
            res1 = max(res1, cnt_1_letter(ch))
        res2 = 0
        # Count balanced substrings containing only pattern[0], pattern[1], and skipping pattern[2].
        for pattern in ["abc", "acb", "bca"]:
            res2 = max(res2, cnt_2_letters(pattern[0], pattern[1], pattern[2]))
        # Count balanced substrings containing all 3 characters.
        res3 = cnt_3_letters("a", "b", "c")

        return max(res1, res2, res3)