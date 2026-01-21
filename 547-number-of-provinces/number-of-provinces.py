from collections import deque

class Solution(object):
    def findCircleNum(self, isConnected):
        province = 0
        n = len(isConnected)
        visited = [False] * n

        def run(start):
            queue = deque([start])
            visited[start] = True

            while queue:
                vertice = queue.popleft()
                for neigh in range(n):
                    if not visited[neigh] and isConnected[vertice][neigh] == 1:
                        visited[neigh] = True
                        queue.append(neigh)

        for i in range(n):
            if not visited[i]:
                province += 1
                run(i)

        return province