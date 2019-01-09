# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def init_intervals(self):
        intervals = []
        for b in ((1,5), (1,1)):
            intervals.append(Interval(b[0], b[1]))
        return intervals

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        l = len(intervals)
        insert_position = -1
        for i in range(l):
            if intervals[i].end < newInterval.start:
                insert_position = i
            else:
                break
        remove_position = insert_position
        for j in range(insert_position+1, l):
            if intervals[j].start <= newInterval.end:
                if intervals[j].start < newInterval.start:
                    newInterval.start = intervals[j].start
                if intervals[j].end > newInterval.end:
                    newInterval.end = intervals[j].end
                remove_position = j
            else:
                break
        return intervals[:insert_position+1]+[newInterval]+intervals[remove_position+1:]


if __name__ == '__main__':
    insert_builder = Solution()
    intervals = insert_builder.init_intervals()
    newInterval = Interval(0,0)
    res = insert_builder.insert(intervals, newInterval)
    print(len(res))

