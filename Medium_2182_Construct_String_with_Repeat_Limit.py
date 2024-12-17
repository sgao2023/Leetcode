# Example: 'aaaaaaabbbbbbbbb', (7 'a' and 9 'b'), repeatLimit = 2. 
# Then the output is expected to be 'bbabbabbabbabaa' (there are 3 'a' unused).
# The way to do it: 
# Put the largest (in this case is 'b') at first (as many as possible), 
# if the number of 'b' reach repeatLimit,
# then concatenate with only 1 'a' (which is the second largest).
# Then follow with 'b'*repeatLimit, then follow with 1 single 'a', and on and on and on... 

# Simulate the above procedure using a while loop.
# In each round, we concatenate either the largest, or the second largest.
# And set the concatenated letter ch as ban, 
# which means ch is banned in the next round.
# In the current round,
# Case 1: if ch is the largest,
# then concatenate ch as many as possible.
# The multiplicity is min(current_number_of_ch, repeatLimit).
# Case 2: if ch is the second largest,
# then only concatenate one single ch,
# we set the multiplicity as mult = 1.
# Ending condition for while loop:
# 1. all letters are exhausted (len(d)==0);
# Or, 2. there's one kind of letter remained, but is banned.
# (len(d) == 1 and max(d.keys())!=ban). 

# Time complexity: O(n)
# Space complexity: the result string takes O(n), the dictionary takes O(1) (at most 26 letters).

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    from collections import Counter    
    d = Counter(s)
    res = ''
    ban = None
    while len(d)>=2 or (len(d) == 1 and max(d.keys())!=ban):
        sort_keys = sorted([k for k in d.keys()])
        if ban == sort_keys[-1]:
            ch = sort_keys[-2]
            mult = 1
        else:
            ch = sort_keys[-1]
            mult = min(d[ch],repeatLimit)
        d[ch] -= mult
        if d[ch] == 0:
            del d[ch]
        res = res+(ch*mult)
        ban = ch
    return res

retu = repeatLimitedString('aaaaaaabbbbbbbbb',2)
print(retu)
        
