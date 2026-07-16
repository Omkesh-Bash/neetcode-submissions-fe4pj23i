class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_list = defaultdict(list)

        for u, v in tickets:
            adj_list[u].append(v)

        result = ["JFK"]

        def dfs(u : str):
            if len(result) == 1 + len(tickets):
                return True

            if not adj_list[u]:
                return False
            
            temp = adj_list[u].copy()
            for i, v in enumerate(temp):
                adj_list[u].pop(i)
                result.append(v)
                if dfs(v) : return True
                adj_list[u].insert(i, v)
                result.pop()
        dfs("JFK")
        return result