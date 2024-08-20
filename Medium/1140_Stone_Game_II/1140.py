#URL : https://leetcode.com/problems/stone-game-ii/description/?envType=daily-question&envId=2024-08-20
#[Medium] [1140] 
#Title: [Stone Game II]
#Author: Kartik Bhatnagar
#Date : 2024-08-20 (YYYY-MM-DD)
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        #using dfs recurion, finding max stones piled up for each possible way
        i =0#start index of piles
        M = 1 #inital m value
        alice_yes =True
        def dfs(i,M,alice_yes):
            print(f"<<<<i:{i} M:{M} Alice{alice_yes}")
            # return 0
            if i>= len(piles):
                print(f"i:{i} m:{M}>>>")
                return 0
            
            # stone_count = max(
            # [sum(piles[i:X])+ dfs(i+X,max(M,X),False) for X in range(1,min(2*M,len(piles))+1)]
            # )
            max_stones,cur_stone_count,cur_stone_count = 0,0,0
            selc_cur_stone_count,selc_dfs_stone_count=0,0
            for X in range(1,min(2*M,len(piles))+1):
                if i+X <= len(piles):
                    cur_stone_count = sum(piles[i:i+X])
                    print(f"X: {X} 2M: {2*M}")
                    print(f"**piles : {piles[i:i+X]}")
                    dfs_stone_count = dfs(i+(i+X-i),max(M,X),not alice_yes)
                    print("^^^^ dfs count: ",dfs_stone_count,"cur count: ",cur_stone_count)
                    if (dfs_stone_count+cur_stone_count) > max_stones:
                        selc_X = X
                        selc_cur_stone_count = cur_stone_count
                        selc_dfs_stone_count = dfs_stone_count
                        max_stones =(dfs_stone_count+cur_stone_count) 
                    
            if alice_yes:
                print(f"i:{i} M:{M} Alice{alice_yes} Ret {selc_cur_stone_count+selc_dfs_stone_count}>>>>>")
                return selc_cur_stone_count+selc_dfs_stone_count
                
            if not alice_yes:#if Bob is picking up stones, no need to add his stone count to return for final
                print(f"i:{i} M:{M} Alice{alice_yes} Ret {selc_dfs_stone_count} >>>>")

                return selc_dfs_stone_count
            
        result = max(
            [sum(piles[i:X])+ dfs(i+X,max(M,X),False) for X in range(1,min(2*M,len(piles))+1)]
            )
        # print("@1",dfs(1,1,False))
        # print("@2",dfs(2,2,False))
        return result
        # return 0

if __name__ == "__main__":
    s=Solution()
    piles = [2,7,9,3,4]
    print(s.stoneGameII(piles))
