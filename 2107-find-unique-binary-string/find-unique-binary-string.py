class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        answer = []
        for i in range(len(nums)):
            if nums[i][i] == "0":
                answer.append("1")
            else:
                answer.append("0")
        return "".join(answer)