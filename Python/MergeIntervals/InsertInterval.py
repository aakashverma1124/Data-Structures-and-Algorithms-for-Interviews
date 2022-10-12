class Innoskrit:
    def insert(self, intervals, newInterval):
        
        i = 0
        ans = []
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
            
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)
        
        while i < len(intervals):
            ans.append(intervals[i])
            i += 1
            
        return ans

if __name__ == "__main__":
    intervals = [[1, 3], [5, 7], [8, 12]]
    newInterval = [4, 6]
    for interval in Innoskrit().insert(intervals, newInterval):
        print(interval, end = " ")
    print()
        