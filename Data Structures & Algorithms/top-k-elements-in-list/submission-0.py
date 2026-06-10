class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        out = []
        for i in range(len(nums)):
            if nums[i] in freq.keys():
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        ordered = sorted(freq.items(), key=lambda x: x[1])[::-1]
        count = 0
        for tup in ordered:
            out.append(tup[0])
            count+=1 
            if count == k:
                break
        return out


        

        