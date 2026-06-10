class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        while len(strs) > 0:
                init = strs[0]
                ana = [strs[0]]
                for i in range(1, len(strs)):
                    if sorted(strs[i]) == sorted(init):
                        ana.append(strs[i])
                for elem in ana:
                    if elem in strs:
                        strs.remove(elem)
                out.append(ana)
        return out



        