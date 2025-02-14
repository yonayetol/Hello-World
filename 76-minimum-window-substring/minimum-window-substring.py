class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        window_counter = Counter()
        def my_comparator(dict1,dict2):
            for k,v in dict2.items():
                if dict1.get(k,0) < v:
                    return False
            return True
            
        answer,left = float('inf'),0
        correct = 0,0
        for right in range(len(s)):
            window_counter[s[right]] += 1
            
            while my_comparator(window_counter,t_counter):
                if right-left+1 < answer:
                    answer = right-left+1
                    correct = left,right+1
                window_counter[s[left]] -= 1
                if window_counter[s[left]] == 0:
                    del window_counter[s[left]]
                left += 1

        return s[correct[0]:correct[1]]