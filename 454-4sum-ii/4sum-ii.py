class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        My_dict = Counter()
        # dict for 1 and 2

        # 1-2= 1 => -1:1
        # 1-1= 0 => 0:1
        # 2-2= 0 => 0:2
        # 2-1= 1 => -1:2
        for i in nums1:
            for j in nums2:
                My_dict[-(i+j)] += 1
        # after doing these
        #nested loop on 3 and 4
        count = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                x = nums3[i]+nums4[j]
                if x in My_dict:
                    count += My_dict[x]
        return count