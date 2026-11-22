class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        n, m = len(version1), len(version2)
        
        while i < n or j < m:
            v1 = 0
            while i < n and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
                
            v2 = 0
            while j < m and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
                
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
                
            i += 1  
            j += 1  
            
        return 0
