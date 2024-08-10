import time
class Solution:
    def get_next_direction(self,cur_dir):
        return self.directions[(cur_dir+1)%self.len_directions]
    
    def get_prev_direction(self,cur_dir):
        return self.directions[(cur_dir)-1]

    def enter_back(self,r_pos,c_pos,tar_dir):
        #when we walkout outside of matrix then find a postion to enter back to matrix
        find_open =True
        while (find_open):
            res = self.direction_fxn[tar_dir](r_pos,c_pos)
            if res[0]:#if empty cell is found; the cell which is not walked before
                find_open=False
                return ([self.get_next_direction(tar_dir),res[1]])
            elif res[1] ==0:#reached to boundary , need to change the direction
                tar_dir = self.get_next_direction(tar_dir)
            else: #if the cell is walked before
                r_pos,c_pos = res[2]
                pass #keep moving in this direction
        return None

    def move_east(self,r_pos,c_pos):
        if ((c_pos+1 < self.cols) and [r_pos,c_pos+1] not in self.path):
            #the new pos should be within the matrix boundary AND new pos cell should not have been visited before
            return ([True,[r_pos,c_pos+1]])
        elif(c_pos+1 >= self.cols) :# walking out of boundary
            return([None,0])
        else: #element is already added to walking path
            return ([None,1,[r_pos,c_pos+1]])
    def move_south(self,r_pos,c_pos):
        if ((r_pos+1 < self.rows) and [r_pos+1,c_pos] not in self.path):
            return ([True,[r_pos+1,c_pos]]) 
        elif(r_pos+1 >= self.rows):
            return([None,0])
        else:
            return ([None,1,[r_pos+1,c_pos]])
    def move_west(self,r_pos,c_pos):
        if ((c_pos-1 >= 0 ) and [r_pos,c_pos-1] not in self.path):
            return ([True,[r_pos,c_pos-1]]) 
        elif(c_pos-1 < 0 ):
            return([None,0])
        else:
            return ([None,1,[r_pos,c_pos-1]]) 
    def move_north(self,r_pos,c_pos):
        if ((r_pos-1 >= 0) and [r_pos-1,c_pos] not in self.path):
            return ([True,[r_pos-1,c_pos]]) 
        elif(r_pos-1 < 0) :
            return([None,0])
        else:
            return ([None,1,[r_pos-1,c_pos]]) 

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):# -> List[List[int]]:
        
        self.rows = rows
        self.cols =cols
        self.directions =[0,1,2,3]#East, south, west, north
        self.len_directions = len(self.directions)
        self.direction_fxn = [self.move_east,self.move_south,self.move_west,self.move_north]
        self.path =[[rStart,cStart]]
        tot_cells = rows*cols
        tar_dir =0 #we will start moving with the east direction from the initail position
        while (len(self.path) < tot_cells):
            print("*"*100)
            print(f"Path : {self.path} \n targetdirection : {tar_dir}")
            res_move = self.direction_fxn[tar_dir](self.path[-1][0],self.path[-1][1])
            print(res_move,self.direction_fxn[tar_dir])
            if res_move[0]:#if empty cell is found; the cell which is not walked before
                self.path.append(res_move[1])
                tar_dir = self.get_next_direction(tar_dir)
            elif res_move[1] ==0:#reached to boundary , need to change the direction
                print("!!!!!!!________Boundary______________")
                out_res = self.enter_back(self.path[-1][0],self.path[-1][1],tar_dir)
                self.path.append(out_res[1])
                tar_dir = out_res[0]
            else: #if the cell is walked before #keep moving in the prev assigned direction
                print("!!!Prev-dir")
                prev_dir = self.get_prev_direction(tar_dir)
                print(f"target : {tar_dir}, prev : {prev_dir}")
                p_res_move = self.direction_fxn[prev_dir](self.path[-1][0],self.path[-1][1])
                if p_res_move[0]:
                    self.path.append(p_res_move[1])
                elif p_res_move[1] ==0:#reached to boundary , need to change the direction
                    print("!!!!!!!________InBoundary______________")
                    out_res = self.enter_back(self.path[-1][0],self.path[-1][1],tar_dir)
                    self.path.append(out_res[1])
                    tar_dir = self.get_next_direction(out_res[0])
                

        
        return self.path

if __name__ == "__main__":
    sol = Solution()
    # print(sol.spiralMatrixIII(5,6,1,4))
    print(sol.spiralMatrixIII(1,4,0,0))
    print(sol.spiralMatrixIII(3,3,0,2))





        