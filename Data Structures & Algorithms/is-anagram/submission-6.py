class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a, b = {}, {}
        for i in range(len(s)):
            a[s[i]] = 1 + a.get(s[i], 0)
            b[t[i]] = 1 + b.get(t[i], 0)
        for i in a:
            if a[i] != b.get(i, 0):
                return False
            
        return True    

        

        
        
        
        """
        Original solution
        list = []
        for i in range(len(s)):
            list.append(s[i:i+1]) 
        for i in range(len(t)):
            if t[i:i+1] in list:
                list.remove(t[i:i+1])
            else:
                return False
        return len(list) == 0
        """
        