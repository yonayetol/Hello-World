import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        
        # Build the graph
        for u, v, w in edges:
            graph.setdefault(u, []).append((v, w))        # Original edge u -> v with cost w
            graph.setdefault(v, []).append((u, 2 * w))    # Reverse edge v -> u with cost 2 * w

        # Initialize the min-heap for Dijkstra's algorithm
        min_heap = [(0, 0)]  # (cost, node)
        min_cost = {i: float('inf') for i in range(n)}
        min_cost[0] = 0

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            # If we pop a node that has a cost more than what we already recorded, we've reached a stale entry
            if cost > min_cost[node]:
                continue

            # Explore neighbors
            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost + edge_cost

                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor))

        # Return minimum cost to reach destination node n-1, or -1 if unreachable
        return min_cost[n - 1] if min_cost[n - 1] < float('inf') else -1