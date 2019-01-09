# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def init_intervals(self):
        intervals = []
        for boundary in ((2,3), (1,4)):
            intervals.append(Interval(boundary[0], boundary[1]))
        return intervals

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                if res[-1].end < intervals[i].end:
                    res[-1].end = intervals[i].end
            else:
                res.append(intervals[i])
        return res



if __name__ == '__main__':
    restructor = Solution()
    intervals = restructor.init_intervals()
    print(len(intervals))
    intervals = restructor.merge(intervals)
    print(len(intervals))
    print(intervals[0].end)

