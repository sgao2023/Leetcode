# Idea:
1. Sliding Window.
2. Use SortedList to maintain max(window)-min(window). 
3. Xor of subarray converts to xor of two prefix_xor values.
4. Implement a Trie to calculate max_xor efficiently. 
5. A better data structure to maintain max(window)-min(window) is the monotonic queue. See https://leetcode.com/problems/sliding-window-maximum/description/

Here to make the solution clear and easy to understand, I use SortedList instead of monotonic queue. 
