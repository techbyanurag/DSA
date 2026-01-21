class DSU:
    def __init__(self):
        # parent[x] = (parent_node, weight)
        # weight = x / parent[x]
        self.parent = {}

    def find(self, x):
        """
        Returns:
        (root, weight_from_x_to_root)
        """
        if x not in self.parent:
            self.parent[x] = (x, 1.0)

        parent, weight = self.parent[x]
        if parent != x:
            root, root_weight = self.find(parent)
            # Path compression with weight update
            self.parent[x] = (root, weight * root_weight)

        return self.parent[x]

    def union(self, x, y, value):
        """
        Given x / y = value
        """
        root_x, weight_x = self.find(x)
        root_y, weight_y = self.find(y)

        if root_x == root_y:
            return

        # Attach root_x under root_y
        # We want:
        #   x / y = value
        #   (x / root_x) * (root_x / root_y) / (y / root_y) = value
        #
        # => root_x / root_y = value * weight_y / weight_x
        self.parent[root_x] = (
            root_y,
            value * weight_y / weight_x
        )

        
class Solution:
    def calcEquation(self, equations, values, queries):
        dsu = DSU()

        # Build DSU
        for (a, b), val in zip(equations, values):
            dsu.union(a, b, val)

        res = []
        for a, b in queries:
            if a not in dsu.parent or b not in dsu.parent:
                res.append(-1.0)
                continue

            root_a, weight_a = dsu.find(a)
            root_b, weight_b = dsu.find(b)

            if root_a != root_b:
                res.append(-1.0)
            else:
                res.append(weight_a / weight_b)

        return res