class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        dicts = {}

        for string in strs:
            letters = {}
            

            for char in string:
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1

            lTuple = tuple(sorted(letters.items()))
            

            if len(dicts) > 0:
            
                if lTuple in dicts:
                    dicts[lTuple].append(string)
                else:
                    dicts[lTuple] = [string]
            else:
                dicts[lTuple] = [string]
                
        
        for value in dicts.values():
            res.append(value)

        return res