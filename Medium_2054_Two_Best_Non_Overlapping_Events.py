# The three methods correspond to functions maxTwoEvents1, maxTwoEvents2, maxTwoEvents3.
# The first method is sorting + prefix sum + binary search. 
# The second method is an improvement of the first one.
# The third method is sort + priority queue. 
# The original post for the third method is:
# https://leetcode.cn/problems/two-best-non-overlapping-events/solutions/1075386/yong-you-xian-dui-lie-wei-hu-ling-yi-ge-8ld3x/
# The author used Go language to write it. 
# I translate it to python and post here.  
def maxTwoEvents1(events: list[list[int]]) -> int:
    # Sorting takes O(n*logn) time and O(n) space.
    by_start = sorted(events, key = lambda x:x[0])
    by_end = sorted(events, key = lambda x:x[1])
    
    pre_max_end = [0]*len(events)
    suf_max_start = [0]*len(events)
    
    # Making maximum prefix/suffix series takes O(n) time.
    mx = 0
    for i in range(len(by_end)):
        ev = by_end[i]
        if ev[2]>=mx:
            mx = ev[2]
        pre_max_end[i] = mx
    mx = 0
    for i in range(len(by_start)-1,-1,-1):
        ev = by_start[i]
        if ev[2]>=mx:
            mx = ev[2]
        suf_max_start[i] = mx
    # Attention: the "sorted" lists by_start and by_end are shallow copies, making prefix or suffix in-place will cause mistakes.
    #(The following annotated code is problematic.)
    #mx = 0
    #for ev in by_end:
    #        if ev[2]>=mx:
    #            mx = ev[2]
    #        else:
    #            ev[2] = mx
    #mx = 0
    #for i in range(len(by_start)-1,-1,-1):
    #    ev = by_start[i]
    #    if ev[2]>=mx:
    #        mx = ev[2]
    #    else:
    #        ev[2] = mx

    # Binary search function, which searches the first index j such that nums[j][i]>=target. 
    # The parameter i takes 0 or 1, corresponds to start time or end time of an event.
    # If no number is greater than i, then return len(nums). 
    def lower_bound(nums,target,i):
        left,right = -1,len(nums)
        while left+1<right:
            mid = left+(right-left)//2
            if nums[mid][i]>=target:
                right = mid
            else:
                left = mid
        return right
    
    # Iterate the events, for each ev in events, find events with end time<=ev[0] or start time>=ev[1]. The maximum values among these events are stored in the prefix/suffix series made at the beginning. 
    # This process takes O(n*logn) time, since the for loop takes O(n) and the binary search takes O(logn).
    ans = 0
    for ev in events:
        val = ev[2]
        ans = max(ans,val)
        ind1 = lower_bound(by_end,ev[0],1)-1
        if ind1>=0:
            val1 = pre_max_end[ind1]
            ans = max(ans,val+val1)
        ind2 = lower_bound(by_start,ev[1]+1,0)
        if ind2<len(events):
            val2 = suf_max_start[ind2]
            ans = max(ans,val+val2)
    return ans

# Improvement: Actually we don't need to consider both of events happen before and events happen after.
# We only need to consider one of them, say events happen after ev. 
# That's because the events happen before ev are already iterated during the outer for-loop.
# This improvement saves half of the running time.
def maxTwoEvents2(events: list[list[int]]) -> int:
    # Sorting takes O(n*logn) time and O(n) space (python sorting takes O(n) space in the worst situation).
    events.sort(key=lambda x:x[0])
    
    suf_max_start = [0]*len(events)
    
    # Making maximum suffix series takes O(n) time.
    mx = 0
    for i in range(len(events)-1,-1,-1):
        ev = events[i]
        if ev[2]>=mx:
            mx = ev[2]
        suf_max_start[i] = mx

    # Binary search function, which searches the first index j such that nums[j][i]>=target. 
    # The parameter i takes 0 or 1, corresponds to start time or end time of an event.
    # If no number is greater than i, then return len(nums). 
    def lower_bound(nums,target,i):
        left,right = -1,len(nums)
        while left+1<right:
            mid = left+(right-left)//2
            if nums[mid][i]>=target:
                right = mid
            else:
                left = mid
        return right
    
    # Iterate the events, for each ev in events, find events with start time>=ev[1]. The maximum values among these events are stored in the suffix series made at the beginning. 
    # This process takes O(n*logn) time, since the for loop takes O(n) and the binary search takes O(logn).
    ans = 0
    for ev in events:
        val = ev[2]
        ans = max(ans,val)
        ind = lower_bound(events,ev[1]+1,0)
        if ind<len(events):
            val2 = suf_max_start[ind]
            ans = max(ans,val+val2)
    return ans

def maxTwoEvents3(events: list[list[int]]) -> int:
    import heapq
    # Elements in hp have the tuple form (end,val).
    hp = []
    #sort by start time
    events.sort()
    ans = 0
    # maxPre keeps track of the maximal value before the current event.
    maxPre = 0
    for ev in events:
        start,end,val = ev[0],ev[1],ev[2]
        # We only need to care about the maximal value of the events happened before the current event, 
        # maxPre tracks that.
        # The elements in hp has the form (end,value). 
        # So, hp[0][0] means the event in hp that ends the earliest. 
        # For the current event we are iterating, i.e., "ev", 
        # we want to get the maximal value of events ended before it.
        # For the events that have not ended yet, we just leave it in the queue.
        # That's how the priority queue works.
        # After the while-loop, only the pending events left in the queue.
        while hp and hp[0][0]<start:
            maxPre = max(maxPre,heapq.heappop(hp)[1])
        ans = max(ans,maxPre+val)
        heapq.heappush(hp,(end,val))
    return ans

evs = [[66,97,90],[98,98,68],[38,49,63],[91,100,42],[92,100,22],[1,77,50],[64,72,97]]

a1 = maxTwoEvents1(evs)
a2 = maxTwoEvents2(evs)
a3 = maxTwoEvents3(evs)
print(a1,a2,a3)
