class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        for c in s1:
            if c in s1Dict:
                s1Dict[c] += 1
            else:
                s1Dict[c] = 1

        l = 0
        r = l + len(s1) - 1

        while r < len(s2):
            i = l

            count = {}

            while i <= r:
                if s2[i] in s1Dict:
                    if s2[i] in count:
                        count[s2[i]] += 1
                    else:
                        count[s2[i]] = 1
                
                i += 1
                
                if count == s1Dict:
                    return True

            l += 1
            r += 1
        
        return False
        