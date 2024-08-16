#URL : https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
#[Medium] [624] 
#Title: [Maximum Distance in Arrays]
#Author: Kartik Bhatnagar
#Date : 2024-08-16 (YYYY-MM-DD)
class Solution:
    def isval_less_minval(self,value):
        #check if the given value is less than any element in self.min_vals
        for mval in self.min_vals:
            if value<mval:
                return True
        return False
    
    def isval_more_maxval(self,value):
        #check if the given value is greater than any element in self.min_vals
        for mval in self.max_vals:
            if value>mval:
                return True
        return False
    
    def find_max_min_from_max_min_val_list(self,ex1,ex2):
        criss_cross = max(abs(self.max_vals[0]-self.min_vals[1]), abs(self.max_vals[1]-self.min_vals[0]))
        if ex1 and ex2:
            return criss_cross
        elif ex1 and not ex2:
            #min_vals[1] and max_val[1] are of same array
            return max(criss_cross,abs(self.max_vals[0]-self.min_vals[0])  )
        elif ex2 and not ex1:
            #min_vals[0] and max_val[0] are of same array
            return max(criss_cross,abs(self.max_vals[1]-self.min_vals[1])  )
        else:
            return max(criss_cross,abs(self.max_vals[1]-self.min_vals[1]),abs(self.max_vals[0]-self.min_vals[0]))
        
    def find_abs_dist(self,ex1,ex2):
        if len(self.min_vals) == 1:
            return abs(self.max_vals[0]-self.min_vals[0])
        else:
            return self.find_max_min_from_max_min_val_list(ex1,ex2)
        
    def maxDistance(self, arrays: list[list[int]]) -> int:
        self.min_vals,self.max_vals = [arrays[0][0]],[arrays[0][-1]] #maintians the top 2 occuring min and max values
        if len(arrays) ==2 :           
            self.min_vals.append(arrays[1][0])
            self.max_vals.append(arrays[1][-1])
            exchange_one,exchange_two=True,True
            return self.find_abs_dist(exchange_one,exchange_two)

        #each variable will contain a list of max 2 size
        exchange_one,exchange_two=True,False
        #exchnage_one true means min_vals[-1] and max_vals[-1] are of same array
        #exchnage_two true means min_vals[0] and max_vals[0] are of same array
        print(self.min_vals,self.max_vals)
        for i in range(1,len(arrays)):
            #check how many values can be inserted in min_vals or max_vals 
            array_min,array_max=arrays[i][0],arrays[i][-1]
            min_check = self.isval_less_minval(array_min)
            max_check = self.isval_more_maxval(array_max)

            #2 -> both min and max value be inserted
            if min_check and max_check:
                if len(self.min_vals) == 1: #both min amd max lenghts will be same at any given point
                    self.min_vals.insert(0,array_min)
                    self.max_vals.insert(0,array_max)
                    exchange_two =True
                else: # 2 elements are present in min_vals and max_vals
                    if array_min < min(self.min_vals)  and array_max > max(self.max_vals):
                        #both min and max value of arrays are lesser and greater respec. than all ele in min and max list
                        self.min_vals[1] =  self.min_vals[0]
                        self.max_vals[1] =self.max_vals[0]
                        self.min_vals[0],self.max_vals[0] = array_min,array_max
                        exchange_one = exchange_two
                        exchange_two =True
                    elif array_min < min(self.min_vals) :
                        #min value of arrays is minimum among min_vals and max value is between max_vals values

                        #we can reduce the size of min_vals and max_vals
                        self.min_vals =[array_min]
                        max_vals = [max(self.max_vals)]
                        exchange_one=False
                        exchange_one =False

                    elif array_max > max(self.max_vals) :
                        self.max_vals =[array_max]
                        self.min_vals = [min(self.min_vals)]
                        exchange_one=False
                        exchange_one =False
                    else:
                        self.min_vals[1] = array_min
                        self.max_vals[1] = array_max
                        exchange_one =True

            #1-> only min value will be inserted in the min_vals 
            elif min_check and not max_check:
                if len(self.min_vals) == 1:
                    self.min_vals[0] = array_min
                    exchange_one =False
                else: #2 elements are present in min_vals
                    if min(self.min_vals) < array_min:#the new array value to be inserted is between min_vals[0] and min_vals[1]
                        #we are assuming at any time min_vals[0] will be lesser than min_vals[1]
                        self.min_vals[1] == array_min
                        exchange_one = False
                    else:               
                        #array[i][0]  is minimum to both min_vals
                        #min-vals and max_vals will become the length 1
                        self.min_vals =[array_min]
                        self.max_vals =[max(self.max_vals)]
                        exchange_two =False
                        exchange_one=False

            #1-> only max value will be inserted in the max_vals   
            elif max_check and not min_check:
                if len(self.max_vals) == 1:
                    self.max_vals[0] = array_max
                    exchange_one =False
                else: #2 elements are present in max_vals
                    if max(self.max_vals) > array_max:#the new array value to be inserted is between max_vals[0] and max_vals[1]
                        #we are assuming at any time max_vals[0] will be greater than max_vals[1]
                        self.max_vals[1] == array_max
                        exchange_one = False
                    else:               
                        #array[i][-1]  is maximum to both max_vals
                        #min-vals and max_vals will become the length 1
                        self.min_vals =[min(self.min_vals)]
                        self.max_vals =[array_max]
                        exchange_two =False
                        exchange_one=False

            #0-> nothing will be inserted
            else:
                #if array's first element is not in top 2 min element and nor the last element a top2 max element          #can be in top 2 max vals
                pass
            print(f"Array {arrays[i]} min:{self.min_vals} max:{self.max_vals}")
        return self.find_abs_dist(exchange_one,exchange_two)

                

        
if __name__ == "__main__":
    s=Solution()
    arrays = [[1,2,3],[4,5],[1,2,3]]
    #print(s.maxDistance(arrays))
    arrays =[[1,2,3],[20,40,60],[1,2,3],[-7,2,800],[-5,1,700],[-50,2,3],[600,700,8000],[8900,9000],[-100,-100,-100],
             [-110,456,9001]]
    # print(s.maxDistance(arrays))
    arrays=[[1,5],[3,4]]
    # print(s.maxDistance(arrays))
    arrays=[[-1,1],[-3,1,4],[-2,-1,0,2]]
    # print(s.maxDistance(arrays))
    arrays=[[-5],[-9,-8,-7,-5,1,1,1,3],[-10,-7,-6,-6,-6,0,1,3,3],[-10,-8,-7,-2,3,3],[-1,4],[-5,-4,-1]]
    print(s.maxDistance(arrays))
              
