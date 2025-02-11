class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        end_num = len(arr)

        while end_num > 0:
            bigger = 0
            for i in range(end_num):
                if arr[i] > arr[bigger]:
                    bigger = i

            flips.append(bigger+1)
            flips.append(end_num)

            arr = arr[end_num-1:bigger:-1] + arr[:bigger+1] + arr[end_num:]
            end_num -= 1
            print(arr)
        return flips
