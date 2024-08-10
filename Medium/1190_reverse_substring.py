""" 
1190. Reverse Substrings Between Each Pair of Parentheses
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
"""



def reverseParentheses(s: str) -> str:
    temp_lis =[]
    for c in s:
        if c != ")": #if there is any element other than close bracket' ) ' append it to list
            temp_lis.append(c)
        else : #when close bracket element comes then reverse the string in list until open bracket appears
            rev_itr =-1
            while temp_lis[rev_itr] != "(": #loop until open bracket appears
                rev_itr -= 1
            #reverse the list elements from open bracket index to the last index
            temp_lis[rev_itr::1] = temp_lis[-1:rev_itr:-1]
    return "".join(temp_lis)
    
inp_s = ["(abcd)","(u(love)i)","(ed(et(oc))el)"]
for s in inp_s:
    print(f"s: {s} ReverseParantheses :{reverseParentheses(s)}")
