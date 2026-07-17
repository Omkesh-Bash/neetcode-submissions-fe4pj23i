class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_list = defaultdict(list)

        for u, v in tickets:
            adj_list[u].append(v)

        result = []

        def dfs(u : str):
            while adj_list[u]:
                dfs(adj_list[u].pop())
            result.append(u)
        dfs("JFK")
        return result[::-1]