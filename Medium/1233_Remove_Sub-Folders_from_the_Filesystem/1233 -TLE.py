#URL : https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=daily-question&envId=2024-10-25
#[Medium] [1233] 
#Title: [Remove Sub-Folders from the Filesystem]
#Author: Kartik Bhatnagar
#Date : 2024-10-25 (YYYY-MM-DD)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        main_folders =set(folder)
        folder.sort()
        def find_sub(str1,str2):
            # print(f"{str1} VS {str2}")
            if len(str1) < len(str2):
                if str1 == str2[:len(str1) if str2[len(str1)] == "/" else 0]:
                    # print(f"{str1} is main folder")
                    if str2 in main_folders:
                        main_folders.remove(str2)
            elif len(str2) < len(str1):
                if str2 == str1[:len(str2) if str1[len(str2)] == "/" else 0]:
                    # print(f"{str2} is the main folder")
                    if str1 in main_folders:
                        main_folders.remove(str1)
            else:
                pass
                # print("no one")
        for i in range(len(folder)):
            for j in range(i+1,len(folder)):
                if folder[i] in main_folders and folder[j] in main_folders:
                    find_sub(folder[i],folder[j])
        return list(main_folders)

        return result
if __name__ == "__main__":
    s=Solution()
