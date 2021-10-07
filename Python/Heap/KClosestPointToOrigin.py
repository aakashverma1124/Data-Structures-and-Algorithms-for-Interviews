#
# @author
# Aakash Verma
#
# www.innoskrit.in
# Instagram: https://www.instagram.com/aakashverma1102/
# LinkedIn: https://www.linkedin.com/in/aakashverma1124/

from heapq import heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(k):
            x = points[i][0]
            y = points[i][1]
            dis = x*x + y*y
            heappush(max_heap, (-dis, x, y))
        
        for i in range(k, len(points)):
            x = points[i][0]
            y = points[i][1]
            dis = x*x + y*y
            if dis < -max_heap[0][0]:
                heappop(max_heap)
                heappush(max_heap, (-dis, x, y))

        ans = []
        while len(max_heap) != 0:
            temp, x, y = heappop(max_heap)
            ans.append([x, y])
        return ans