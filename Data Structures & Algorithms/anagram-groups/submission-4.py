class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for elem in strs:
            group = 0
            for key in ht:
                if (self.isanagram(elem, key)):
                    ht[key].append(elem)
                    group = 1
                    break
            if (group == 0):
                ht[elem] = [elem]
        lst = []
        for item in ht:
            lst.append(ht[item])
        return lst

    def isanagram(self, str1 : str, str2: str) -> bool:
        ht1 = {}
        ht2 = {}
        for char in str1:
            if char in ht1:
                ht1[char] += 1
            else:
                ht1[char] = 1
        for char in str2:
            if char in ht2:
                ht2[char] += 1
            else:
                ht2[char] = 1
        return ht1 == ht2






        
        