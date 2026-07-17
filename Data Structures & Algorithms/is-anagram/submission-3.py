class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = []
        for i in range(len(s)):
            list.append(s[i:i+1]) 
        for i in range(len(t)):
            if t[i:i+1] in list:
                list.remove(t[i:i+1])
            else:
                return False
        return len(list) == 0