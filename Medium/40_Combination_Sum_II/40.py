#URL : https://leetcode.com/problems/combination-sum-ii/description/
#[Medium] [40] 
#Title: [Combination Sum II]
#Author: Kartik Bhatnagar
#Date : 2024-08-13 (YYYY/MM/DD)

class Solution:
    def contains_sublist(self,lis1,su_lis):
        #if checks if the lis1 [list] is having any combinaiton among su_lis list[list]
        for l in su_lis:
            if sorted(l) == sorted(lis1):
                return False
        return True
            
    def check_sum_to_target(self,val_lis):
        return [val for val in val_lis if val == self.target]
       
    def remove_start_ele(self,start_lis,cand_lis):
        for ele in start_lis:
                cand_lis.remove(ele)
        return cand_lis
    
    def get_combinations_target_less(self):
        all_combinations=[]        
        target_list=[]#result to return #contains the elements in a list whose sum is equivalent to target
        start =list(set(self.candidates))
        # start =self.candidates
        sum_1_target= (self.check_sum_to_target(start))#add this to target_lis
        start = [[s] for s in start]
        all_combinations.extend(start.copy())
        if len(sum_1_target)>0:
            target_list.append(sum_1_target)
        for ele_count in range(1,len(self.candidates)):
            temp_candidates  = [c for c in self.candidates]
            new_start =[]
            for ele_lis_start in start:
            #iterate to element in start add 1 more element to the new_start list from the remaining element of the main candiate list
                #remove the ele_count elements from the temp_candiates
                temp_candidates = self.remove_start_ele(ele_lis_start,temp_candidates)#at the end of the loop add back these elements for next iteration
                #remove duplicate elements from temp_candidates
                temp_candidates_short = list(set(temp_candidates))
                # add back these elements for next iteration
                temp_candidates.extend(ele_lis_start)
                ele_lis_start2= [i for i in ele_lis_start]
                for e in temp_candidates_short:
                    ele_lis_start2.append(e)
                    if sum(ele_lis_start2) <= self.target:# add element only when the list sum is equal to target
                        if self.contains_sublist(ele_lis_start2,new_start):#add element only when the the list elements are unique among whole list
                            new_start.append(ele_lis_start2.copy())
                    ele_lis_start2.remove(e)  
                 
            all_combinations.extend(new_start.copy())
            start =new_start.copy()
        # print(all_combinations)
        return all_combinations
       
       
    def combinationSum2(self, candidates, target) :#-> list[list[int]]:
        if len(candidates)==0:
            return []
        # more than 1 elements
        if len(candidates) == 1:
            if candidates[0] == target:
                return [[target]]
            else:
                return []
        #we need to run the combination algorithm
        self.target = target
        self.candidates = candidates
        all_combination_target_less = self.get_combinations_target_less()
        all_combination=[]
        for lis in all_combination_target_less:
            if sum(lis) == target:
                all_combination.append(lis)
        return all_combination

            

if __name__ =="__main__":
    s1=Solution()
    candidates1 =[2,3,6,1,3,7,8,6,8]
    target1=8
    print(f"Target : {target1} Combinations : {s1.combinationSum2(candidates1,target1)}")
    s2=Solution()
    candidates2=[3,1,3,5,1,1,9]
    target2=9
    print(f"Target : {target2} Combinations : {s2.combinationSum2(candidates2,target2)}")
    s3=Solution()
    candidates3=[1,1]
    target3=2
    print(f"Target : {target3} Combinations : {s3.combinationSum2(candidates3,target3)}")
