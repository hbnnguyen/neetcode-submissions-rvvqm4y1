class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s) - 1
    
        while i < j:
            while i < j and not self.alphaNum(s[i]):
                i += 1
            while j > i and not self.alphaNum(s[j]):
                j -= 1
            
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def alphaNum(self, c):
        alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
        numbers = {"1","2","3","4","5","6","7","8","9","0"}

        if c in alphabet or c in numbers:
            return True
        else:
            return False
