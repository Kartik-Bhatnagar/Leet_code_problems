def make_triangle(tot_rows):
    #tot_rows>0
    ptriangle =[]
    row_count=-1
    cols_ele_count =0
    
    #first row
    if tot_rows>0:
        ptriangle = [[1]]
        row_count+=1
        cols_ele_count +=1
    # first row done    
    
    for r in range(1,tot_rows):
        
        row_count+=1 
        temp_lis =[1]
        cols_ele_count+=1
        for i in range(1,cols_ele_count):
            cur_ele = 1
            if i < len(ptriangle[row_count-1]): #if the current indx is there in previous row
                cur_ele = ptriangle[row_count-1][i] +   ptriangle[row_count-1][i-1]
            temp_lis.append(cur_ele)    
        ptriangle.append(temp_lis)
    return(ptriangle)    

print(make_triangle(5))

            
