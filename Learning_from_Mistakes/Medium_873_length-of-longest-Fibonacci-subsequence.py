# Original post: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solutions/152343/c-java-python-check-pair
# This solution is from leetcode user "lee". 
# In the original post, he shares two methods. The other method is also nice. 
# I post it at the end of this file. 

# Time complexity: O(n^2)
# Space complexity: O(n^2), 
# since the keys of the dictionary subseq_length consist pairs in arr.
# In addition, the set arr_set takes O(n) space.

# The key point of this algorithm is that the last two terms 
# uniquely determine the Fibonacci sequence.
# I didn't notice this point in my first try. That's how I made mistakes.

# The key-value pairs in the dictionary "subseq_length" have the form (y,x):length, 
# where (y,x) are the ending two terms of a Fibonacci sequence.

from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:

        subseq_length = {}
        arr_set = set(arr)
        ans = 0
        for i,x in enumerate(arr):
            for j in range(1,i):
                y = arr[j]
                if x-y in arr_set and x-y<y:
                    if (x-y,y) not in subseq_length:
                        subseq_length[(y,x)] = 3
                    else:
                        subseq_length[(y,x)] = subseq_length[(x-y,y)]+1
                    ans = max(ans,subseq_length[(y,x)])
        return ans

    
        # WRONG ANSWER
        # My first try, which was a wrong answer
        # The idea is to keep track of the length of 
        # longest subsequence ending at every index,
        # and store the information in the dictionary "visited".

        # However, the new term "x" may not be the next element of 
        # the longest Fib subsequence ending at arr[j]. 
        # The key point is that, with only the last term arr[j], 
        # we cannot determine the whole Fibonacci sequence.

        # visited = {}
        # ans = 0
        # for i,x in enumerate(arr):
        #     curr_max_length = 0
        #     for j in range(1,i):
        #         if x-arr[j] in visited and x-arr[j]<arr[j]:

        #             if visited[arr[j]] == 0:
        #                 curr_max_length = max(curr_max_length,3)
        #             else:
        #                 curr_max_length = max(curr_max_length,visited[arr[j]]+1)
        #     visited[x] = curr_max_length
        #     ans = max(ans,curr_max_length)

        # return ans


# Another solution from leetcode user 'lee'.
# This is nice as well. 
# Look at the way he update a,b,l in the while loop.
# Time complexity: O(n^2 log(M)), where M=max(arr).
# Space complexity: O(n). The set s takes O(n) space.
class Solution:
    def lenLongestFibSubseq(self, A):
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0