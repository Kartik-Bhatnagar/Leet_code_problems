from collections import defaultdict

class Solution:
    def __init__(self):
        self.tree = defaultdict(list)
        self.subtree_sizes = {}

    def buildTree(self, edges):
        for a, b in edges:
            self.tree[a].append(b)
            self.tree[b].append(a)

    def dfs(self, node, parent):
        # DFS to calculate the size of each subtree
        subtree_size = 1  # Start with 1 to count the node itself
        for child in self.tree[node]:
            if child != parent:  # Avoid revisiting the parent node
                subtree_size += self.dfs(child, node)
        self.subtree_sizes[node] = subtree_size
        return subtree_size

    def isGoodNode(self, node):
        # Check if all immediate children have the same subtree size
        child_subtree_sizes = []
        for child in self.tree[node]:
            if self.subtree_sizes[child] is not None:
                child_subtree_sizes.append(self.subtree_sizes[child])

        # A node is good if all its children have the same subtree size
        return len(set(child_subtree_sizes)) <= 1

    def countGoodNodes(self, edges: list[list[int]]) -> int:
        self.buildTree(edges)
        self.dfs(0, -1)  # Start DFS from the root node (assumed to be 0)
        good_nodes_count = 0

        for node in range(len(edges) + 1):
            if self.isGoodNode(node):
                good_nodes_count += 1

        return good_nodes_count

# Test cases
sol = Solution()

# Example 1
edges1 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
print(sol.countGoodNodes(edges1))  # Expected output: 7

# Example 2
edges2 = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [1, 6], [2, 7], [3, 8]]
print(sol.countGoodNodes(edges2))  # Expected output: 6

# Example 3
edges3 = [[0, 1], [1, 2], [1, 3], [1, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10], [9, 12], [10, 11]]
print(sol.countGoodNodes(edges3))  # Expected output: 12