def shortestPalindrome(s: str) -> str:
    # What follows is a function that generate the pi array of a pattern (string). 
    def pi(pattern:str)->list[int]:
        c = 0
        m = len(pattern)
        pi = [0]*m
        for i in range(1,m):
            v = pattern[i]
            while c and pattern[c] != v:
                c = pi[c-1]
            if pattern[c] == v:
                c += 1
            pi[i] = c
        return pi
    # Compare s and its inverse t:=s[::-1] .
    # Find the longest common part of s and t.
    # First align s and t at index both=0, 
    # then shift s rightward, using a similar method to KMP algorithm. 
    # How many indices should be shifted?
    # That depends on the pi_list. 
    pi_list = pi(s)
    t=s[::-1]
    m = len(t)
    c = 0
    for i,v in enumerate(t):
        while c and s[c] != v:
            c = pi_list[c-1]
        if s[c] == v:
            c += 1
    # After the last round of the for loop (i.e., i=len(t)-1), 
    # the c value is the length of the longest common part of s and t. 
    # What we want to add at the beginning should be inverse of s[c:]. 
    return s[c:][::-1]+s

new_str = shortestPalindrome('aacecaaab')
print(new_str)