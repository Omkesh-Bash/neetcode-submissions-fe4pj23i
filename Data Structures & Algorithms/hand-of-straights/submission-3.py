class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        count = Counter(hand)
        # print(count)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        # print(list(count.keys()))
        while min_heap:
            removed = []
            for i in range(min_heap[0], min_heap[0] + groupSize):
                # print(len(min_heap))
                if len(min_heap) == 0:
                    return False
                removed.append(heapq.heappop(min_heap))
                # print(i, removed[-1])
                if removed[-1] != i:
                    return False
            for n in removed:
                if count[n] != 1:
                    count[n] -= 1
                    heapq.heappush(min_heap, n)
            # print(min_heap)
        return True
