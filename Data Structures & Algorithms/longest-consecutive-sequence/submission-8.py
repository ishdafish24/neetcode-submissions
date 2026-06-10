class Solution:
    def longestConsecutive(self, nums: List[int])-> int:
        chain_starts = []
        for elem in list(set(nums)):
            if elem - 1 not in list(set(nums)):
                chain_starts.append(elem)
        max_count = 0
        for elem in chain_starts:
                count = 1
                c = 1
                while elem+c in list(set(nums)):
                    count += 1
                    c += 1
                if count > max_count:
                    max_count = count
                count = 1
        return max_count
        """
        max_count = 0
        for elem in list(set(nums)):
                count = 1
                c = 1
                while elem+c in list(set(nums)):
                    count += 1
                    c += 1
                if count > max_count:
                    max_count = count
                count = 1
        return max_count
        """