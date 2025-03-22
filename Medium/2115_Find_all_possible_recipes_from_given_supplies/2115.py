#URL : https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/
#[Medium] [2115] 
#Title: [Find all possible recipes from given supplies]
#Author: Kartik Bhatnagar
#Date : 2025-03-22 (YYYY-MM-DD)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        output = set() #set
        recipe_no = set()
        count =0
        supplies = set(supplies)
        rec_ing  = {r:i for r,i in zip(recipes,ingredients)}

        def supp_available(rec,visited_rec): 
            # print("    ## : ",rec) 
            available = True
            if rec in output:#if the ingrendient is a recipe and its possible to make
                return available
            elif rec in recipe_no: #if the ingrendient is a recipe and its not possible to make then the current recipe is also not possible
                return False
            for ing in rec_ing[rec]:
                print(ing)
                if ing in supplies:
                    continue
                elif ing in output : #an ingredient can be a recipes and that can be in output
                    continue
                elif ing in rec_ing:
                    #check in the recipes and if that recipe is not added in the output 
                    #in dfs manner keep looking for its available supply
                    if ing in visited_rec:
                        return False
                    visited_rec.add(ing)
                    available = supp_available(ing,visited_rec)
                    if not available:
                        recipe_no.add(ing)
                        return False
                    else:
                        output.add(ing)                  
                else:
                    # if any ingredient is not there either in recipe and nor in supplies 
                    available = False
                    return available
            return available
            #if available:
                #output.add(rec)

        for rec in recipes:
            visited = set()
            # print("   **",rec,output)
            ing_available = supp_available(rec,visited)
            if ing_available:
                output.add(rec)

        return list(output)
        
if __name__ == "__main__":
    s=Solution()
