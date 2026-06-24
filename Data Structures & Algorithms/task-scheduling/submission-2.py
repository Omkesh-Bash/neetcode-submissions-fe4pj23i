class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks) # no need to typecast in dict
        time = 0
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)
        q = deque()

        while q or max_heap:
            time += 1
            if max_heap :
                task = heapq.heappop(max_heap) + 1
                if task:
                    q.append((task, n + time))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time 