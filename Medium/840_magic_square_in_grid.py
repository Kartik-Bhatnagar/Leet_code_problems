class Solution:
    def magic_square(self,row_start,row_end,col_start,col_end): #checks if the 3X3 matrix is a magic square or not
        #numbers should be distinct and should be in range (1,9)
        #each row , column and both diagonal should have same sum       
        #____check1____same rows sum for all 3 rows__
        #check row_sum and collect matrix rows for checking distinct elements
        r =row_start
        matrix_3 = []
        full_row = self.grid[r][col_start:col_end+1]
        matrix_3.append(full_row)
        row_sum = sum((full_row))
        r+=1
        r_count=0
        while r_count <2 :#iterate 2 times
            full_row = (self.grid[r][col_start:col_end+1])
            matrix_3.append(full_row)
            if sum(full_row) == row_sum :
                #comapring with the first row sum
                r_count+=1
                r+=1
            else :#if rows sum doesn't match
                return False
        print(matrix_3)     
        #__check2__distinct elements__ and if the numbers are in range(1,9)
        matrix_rows = []
        for rw in matrix_3:
            matrix_rows.extend(rw)
            if len([r for r in rw if r>0 and r<10]) <3:
                #checking if each element in the row is in range(1,9)
                return False
        if len(set(matrix_rows)) != 9:
            #all 9 elements of the row are not distinct
            return False
        
        
        #__check3___column sum , all 3 columns sum same___
        col_sum = sum([c[0] for c in matrix_3])
        if (col_sum != row_sum):
            return False
        c_pos =1
        while c_pos <3:
            if (sum([c[c_pos] for c in matrix_3])) == col_sum:
                c_pos+=1
            else:
                return False
            
        #___check4_both diagnols sum same__
        d1 = [matrix_3[i][i] for i in range(3)]
        if sum(d1) != row_sum:
            return False
        print(row_sum,col_sum,sum(d1))
        d2=[]
        pos=2
        for r in matrix_3:
            d2.append(r[pos])
            pos-=1

        # print(sum(d1),sum(d2))
        if sum(d1) != sum(d2):
            return False
        print(f"d2 :{d2} {sum(d2)}")

        return True
    def check_valid_grid(self):
        #a gird is only valid if it has alteast 3 rows and 3 columns
        if len(self.grid[0]) >=3 and len(self.grid) >=3:
            return True
        else:
            return False

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        self.grid = grid
        if not self.check_valid_grid():
            return 0
        row_start =col_start =0
        magic_mat_count = 0
        #iterating through the sub grids and finding the number of 3X3 magic sqaure matrix
        for col_end in range(2,len(grid[0])): #columns
            row_start=0
            for row_end in range(2,len(grid)):#rows
                print(row_start,row_end,col_start,col_end)
                if self.magic_square(row_start,row_end,col_start,col_end):
                   magic_mat_count +=1
                row_start +=1
            col_start +=1

        return magic_mat_count
if __name__ == "__main__":
    sol = Solution()
    grid1= [[4,3,8,4,5],[9,5,1,9,5],[2,7,6,2,5],[2,7,6,2,5],[2,7,6,2,5],[2,7,6,2,5],[2,7,6,2,5]]
    grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    grid = [[10,3,5],[1,6,11],[7,9,2]]
    print(sol.numMagicSquaresInside(grid))

