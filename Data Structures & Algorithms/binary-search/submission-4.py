class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b_ind = 0
        e_ind = len(nums)-1
        m_ind = int((b_ind + e_ind) / 2)
        while (nums[m_ind] != target):
            if (m_ind == b_ind):
                if (nums[m_ind] == target):
                    return m_ind
                elif (nums[e_ind] == target):
                    return e_ind
                else:
                    return -1
            if nums[m_ind] < target:
                b_ind = m_ind
                m_ind = int((b_ind + e_ind) / 2)
                continue
            else:
                e_ind = m_ind
                m_ind = int((b_ind + e_ind) / 2)
                continue
        return m_ind