class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_ = dict(collections.Counter(tasks))
        max_heap = []
        for value in tasks_.values():
            heapq.heappush(max_heap, -value)
        q = deque()
        time = 0
        while len(max_heap) != 0 or len(q) != 0:
            time += 1
            while len(q) != 0 and q[0][1] == time:
                heapq.heappush(max_heap, q[0][0])
                q.popleft()
            if(max_heap):
                task = heapq.heappop(max_heap) + 1
                if task != 0:
                    q.append((task,time + n + 1))
        return time 