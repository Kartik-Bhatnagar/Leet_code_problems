#URL : https://leetcode.com/problems/all-oone-data-structure/description/?envType=daily-question&envId=2024-09-29
#[Hard] [432] 
#Title: [All O`one Data Structure]
#Author: Kartik Bhatnagar
#Date : 2024-09-29 (YYYY-MM-DD)
class AllOne:

    def __init__(self):
        self.d =dict()

    def inc(self, key: str) -> None:
        self.d[key] = self.d.get(key,0) +1

    def dec(self, key: str) -> None:
        val=self.d.get(key,0)-1
        if val ==0:
            del self.d[key]
        else:
            self.d[key] =val
        

    def getMaxKey(self) -> str:
        if len(self.d.keys()) >0:
            return max(self.d, key=self.d.get)
        else:
            return ""
        

    def getMinKey(self) -> str:
        if len(self.d.keys()) >0:
            return min(self.d, key=self.d.get)
        else:
            return ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
if __name__ == "__main__":
    s=Solution()
