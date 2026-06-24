
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_ = dict(collections.Counter(tasks))
        max_heap = []
        for value in sorted(tasks_.values()):
            heapq.heappush(max_heap, -value)
        q = []
        time = 0
        while len(max_heap) != 0 or len(q) != 0:
            while len(q) != 0 and q[0][1] == time:
                heapq.heappush(max_heap, q[0][0])
                q.pop(0)
            # print(time)
            if(max_heap):
                task = heapq.heappop(max_heap) + 1
                # print('-', task)
                if task != 0:
                    q.append((task,time + n + 1))
            # print(time)
            time += 1
        return time