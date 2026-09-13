"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Min heap Approach
        # intervals.sort(key=lambda x:x.start)
        # min_heap = []
        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval.start:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, interval.end)
        # return len(min_heap)        

        #Sweep Line Algorithm

        # mp = defaultdict(int)
        # for i in intervals:
        #     mp[i.start] += 1
        #     mp[i.end] -= 1
        # prev = 0
        # res = 0
        # for i in sorted(mp.keys()):
        #     prev += mp[i]
        #     res = max(res, prev)
        # return res

        #Two Pointer Approach

        #Greedy Approach
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))
        time.sort(key= lambda x:(x[0], x[1]))
        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res

        