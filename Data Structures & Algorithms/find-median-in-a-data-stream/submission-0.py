
class MedianFinder:

    def get_at_index(self, lst, index, default) -> float:
        try:
            return lst[index]
        except IndexError:
            return default

    def __init__(self):
        self.small_heap, self.large_heap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, -num)
        # right elements
        
        if(-self.small_heap[0] > self.get_at_index(self.large_heap, 0, 100000)): # its ok if they are equal
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        
        # balance
        bf = len(self.small_heap) - len(self.large_heap)
        if(bf > 1): # small_heap is bigger
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        elif(bf < -1): # large_heap is bigger
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))


    def findMedian(self) -> float:
        # balance
        bf = len(self.small_heap) - len(self.large_heap)
        if(bf == 1): # small_heap is bigger
            return -self.small_heap[0]
        elif(bf == -1): # large_heap is bigger
            return self.get_at_index(self.large_heap, 0, 100000)
        else:
            return ((-self.small_heap[0]) + self.large_heap[0]) / 2

