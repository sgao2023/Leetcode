# Idea:

Suppose that in Counter(nums) sorted by frequency values, we have a_1 with multiplicity f_1, a_2 with mult'y f_2, ... , a_k with mult'y f_k, where f_1 <= f_2 <= ... <= f_k.

Case 1. f_k >= (f_1 + ... + f_(k-1))

If this is the case, then we pair everything else with a_k.
Finally, there will be f_k - (f_1 + ... + f_(k-1)) numbers left.

Case 2. f_k < (f_1 + ... + f_(k-1))

In this situation, we have the following claim:
The minimum length of nums after applying the operateion zero or more times is len(nums) % 2. 

Proof: Use math induction on diff := (f_1 + ... + f_(k-1)) - f_k. 
I present the case for len(nums) is even. (Proof of odd case is similar.) 
Prove for diff == 2: Take any two indices i and j, remove the pair (a_i, a_j). Then the new_diff == old_diff - 2 = 0. Then by the above Case 1, finally there's nothing left.

Suppose that the claim is true for all even diff <= 2 * k. Now we look at diff == 2 * (k+1). Again, cancel a pair (a_i, a_j), we get a new_diff == old_diff - 2. Now we can use our hypothesis for diff <= 2 * k. 

Q.E.D.