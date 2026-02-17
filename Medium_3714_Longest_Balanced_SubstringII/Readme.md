The idea of my solution follows from https://leetcode.cn/problems/longest-balanced-substring-ii/solutions/3803790/shi-zi-bian-xing-mei-ju-you-wei-hu-zuo-p-slnc/

# Idea

Unlike problem 3713, here in this problem, the string only contains "a", "b", "c".

A balanced substring can be one of the 3 following cases:

1. It contains only one kind of character.
2. It contains two kinds of characters.
3. It contains all 3 characters.

We handle these 3 cases separately.

For cases 2 and 3, we proceed with prefix sum. 

Take case 3 for example: 

We iterate through the string s and get (cnt_a, cnt_b, cnt_c). We store the key-value pair (0, cnt_b-cnt_a, cnt_c-cnt_a) -> i in a dictionary, where "i" is the first occurrence of the triple. When we reach index i, if the triple (0, cnt_b-cnt_a, cnt_c-cnt_a) already exists in the dict (with value "left"), then the slice [left, i] is a balanced substring. 