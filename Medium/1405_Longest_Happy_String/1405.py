#URL : https://leetcode.com/problems/longest-happy-string/editorial/?envType=daily-question&envId=2024-10-16
#[Medium] [1405] 
#Title: [Longest Happy String]
#Author: Kartik Bhatnagar
#Date : 2024-10-16 (YYYY-MM-DD)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result =""
        while([a,b,c].count(0)<2):
            max1 = max(a,b,c)#first max
            if max1 == a:
                count1 = 2 if a>1 else 1
                result+=count1*"a"
                max1_char ="a"
            elif max1 ==b:
                count1 = 2 if b>1 else 1
                result+=count1*"b"
                max1_char="b"
            else:
                count1 = 2 if c>1 else 1
                result+=count1*"c"
                max1_char="c"
            
            #find second highest
            l=[a,b,c]
            l.remove(max(a,b,c))
            max2= max(l)
            count2 = 2 if max1-max2 <=1 else 1
            if max1_char =="a":
                if max2 == b:
                    if count2==2:
                            count2 = 2 if b>1 else 1
                    result += count2*"b"
                    max2_char ="b"
                else:
                    if count2==2:
                            count2 = 2 if c>1 else 1
                    result +=count2 * "c"
                    max2_char ="c"
            elif max1_char =="b":
                if max2 == a:
                    if count2==2:
                            count2 = 2 if a>1 else 1
                    result += count2*"a"
                    max2_char ="a"
                else:
                    if count2==2:
                            count2 = 2 if c>1 else 1
                    result +=count2 * "c"
                    max2_char ="c"
            else:
                if max2 == a:
                    if count2==2:
                            count2 = 2 if a>1 else 1
                    result += count2*"a"
                    max2_char ="a"
                else:
                    if count2==2:
                            count2 = 2 if b>1 else 1
                    result +=count2 * "b"
                    max2_char ="b"
            max3_char=None
            if count2>1:
                #find third highest
                max3_char =[i for i in ["a","b","c"] if i!= max2_char and i!=max1_char][0]
                l.remove(max2)
                max3=l[0]
                print("^",max3_char)
                count3 = 1 if max2-max1 > 2 else 2
                if max3_char =="a":
                    if a>0:
                        if count3==2:
                            count3 = 2 if a>1 else max(1,a)
                            print("$$",count3)
                            result += count3*"a"
                    else:
                        count3 =0
                elif max3_char =="b":
                    if b>0:
                        if count3==2:
                            count3 = 2 if b>1 else 1
                            result += count3*"b"
                    else:
                        count3 =0
                elif max3_char =="c":
                    if c>0:
                        if count3==2:
                            count3 = 2 if c>1 else 1
                            result += count3*"c"
                    else:
                        count3=0
                        
                
            print(result)
            print("*",a,b,c)
            #removing counts
            if max1_char =="a":
                a-= count1
            elif max1_char =="b":
                b-= count1
            else:
                c-=count1
            if max2_char =="a":
                a-= count2
            elif max2_char =="b":
                b-= count2
            else:
                c-=count2
            if max3_char != None:
                print("***",max3_char,count3)
                if max3_char =="a":
                    a-= count3
                elif max3_char =="b":
                    b-= count3
                else:
                    c-=count3
                
            print(a,b,c)
        if len(result) ==0:    
            if a>0:
                count = 2 if a>1 else 1
                result += count*"a"
            elif b>0:
                count = 2 if b>1 else 1
                result += count*"b"
            else:
                count = 2 if c>1 else 1
                result += count*"c"
        elif a >0:
            if result[-1]!="a":
                count = 2 if a>1 else 1
                result += count*"a"
        elif b>0:
            if result[-1]!="b":
                count = 2 if b>1 else 1
                result += count*"b"
        elif c >0:
            if result[-1]!="c":
                count = 2 if c>1 else 1
                result += count*"c"
        return result




if __name__ == "__main__":
    s=Solution()
