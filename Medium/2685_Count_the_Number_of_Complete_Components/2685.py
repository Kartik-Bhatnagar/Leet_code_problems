#URL : https://leetcode.com/problems/count-the-number-of-complete-components/submissions/1582288502/?envType=daily-question&envId=2025-03-22
#[Medium] [2685] 
#Title: [Count the Number of Complete Components]
#Author: Kartik Bhatnagar
#Date : 2025-03-22 (YYYY-MM-DD)
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #1) create a lookup dict
        lookup ={i:set() for i in range(n)}
        for edge in edges:
                lookup[edge[0]].add(edge[1])
                lookup[edge[1]].add(edge[0])
        print(lookup)
        # c_lookup ={i:set() for i in range(n)}
        #2) check the potential connected groups
        def dfs_look(edge,connected):
            visited.add(edge)
            connected.add(edge)
            for com in lookup[edge]:
                if com not in visited:
                    connected = dfs_look(com,connected)                    
            return connected

        visited = set()
        all_connected =[]
        for edge,comps in lookup.items():
            if edge not in visited:            
                connected = dfs_look(edge,set([edge]))
                all_connected.append(connected)
        print(all_connected)
        #3) check the number of true connected components
        #for each connected components, count the number of edges
        #if number of edges are equal to m*(m-1)
        result = 0
        for connected in all_connected:
            tot_edges = 0
            for edge in connected:
                tot_edges= tot_edges + len(lookup[edge])
            # print(tot_edges)
            if tot_edges  == len(connected) * (len(connected) -1):
                result +=1
        return result

            
                    



        #count the total connected groups
if __name__ == "__main__":
    s=Solution()
