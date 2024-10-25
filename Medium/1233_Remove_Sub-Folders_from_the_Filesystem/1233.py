#URL : https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=daily-question&envId=2024-10-25
#[Medium] [1233] 
#Title: [Remove Sub-Folders from the Filesystem]
#Author: Kartik Bhatnagar
#Date : 2024-10-25 (YYYY-MM-DD)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the folders to ensure subfolders come immediately after their parent
        folder.sort()
        print(folder)
        result = []

        # Add the first folder to the result as it is definitely not a subfolder
        result.append(folder[0])

        # Iterate over the sorted folder list and check if the current folder is a subfolder
        for i in range(1, len(folder)):
            # Check if the current folder starts with the last added folder in the result
            # and is followed by a '/'
            if not folder[i].startswith(result[-1] + '/'):
                result.append(folder[i])

        return result
if __name__ == "__main__":
    s=Solution()
