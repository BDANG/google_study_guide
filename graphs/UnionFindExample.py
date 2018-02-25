# https://leetcode.com/problems/redundant-connection/description/
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        parent = {}
        def find(u):
            if u not in parent.keys():
                parent[u] = -1
                return u
            elif parent[u] == -1:
                return u
            else:
                return find(parent[u])

        def union(u, v):
            parent[find(u)] = find(v)


        for edge in edges:
            if find(edge[0]) == find(edge[1]):
                return edge
            else:
                union(edge[0], edge[1])
