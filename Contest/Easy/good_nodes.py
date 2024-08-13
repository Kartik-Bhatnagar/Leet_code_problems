class Solution:
    def nodeChildCount(self,node):
        #returns the count of immediate childeren of the node
        return len([c for c in self.edges if c[0] == node])
        # cnode_count=0
        # for edge in self.edges():
        #     if edge[0] == node:
        #         cnode_count
    def immediateChild(self,node):
        #returns the list of nodes immediate child
        child =[]
        for edge in self.edges:
            if edge[0] == node:
                child.append(edge[1])
        return child
    def subTreeNodeCount(self,node):
        #returns the count of all nodes present in the subtree with node as root
        node_count=0
        def dfs(rnode):
            nonlocal node_count
            child_nodes = self.immediateChild(rnode)
            if len(child_nodes)>0:
                for child in child_nodes:
                    dfs(child)
                    node_count +=1
            else:
                return
        roo_child_nodes = self.immediateChild(node)
        for cnode in roo_child_nodes:
            dfs(cnode)
            node_count+=1
        return node_count

    def goodNode(self,node):
        #returns true if a node is a good node
        #if the child count of the node is 0 ,1 or equal number of childs for all immediate children of the node  then the node is a good node
        child_count = self.nodeChildCount(node)
        if child_count <2:
            return True
        else:
            child_nodes = self.immediateChild(node)
            subtree_node_count = self.subTreeNodeCount(child_nodes[0])
            for i in range(1,child_count):
                if subtree_node_count != self.subTreeNodeCount(child_nodes[i]):
                    #if all immediate children has not the same subtreecount 
                    return False
            return True
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        #if a node has equal
        self.edges = edges
        good_nodes_count=0
        for node in range(len(edges)+1):
            if (self.goodNode(node)):
                good_nodes_count +=1

        return good_nodes_count

if __name__ =="__main__":
    s1= Solution()
    edges1 = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    edges2=[[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
    edges3=[[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
    edges4=[[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]
    # print(s1.countGoodNodes(edges1))  
    # print(s1.subTreeNodeCount(0))      
    # print(s1.countGoodNodes(edges2))
    # print(s1.subTreeNodeCount(0))
    # print(s1.countGoodNodes(edges3))
    print(s1.countGoodNodes(edges4))