class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        int length = queries.size();
        vector<bool> answer;
        int parity = nums[0]%2; 
        int incr = 0;
        nums[0] = incr++;
        for (int m=1;m<nums.size();m++){
            if (nums[m]%2 != parity)
                {parity = ((nums[m])%2);
                nums[m] = incr++;}
                
            else
                nums[m] = incr-1;
            
        }

        for (int i=0;i<length;i++){
            int from = queries[i][0],to = queries[i][1];
            bool tempo = true;
            if ((from - to) != (nums[from]-nums[to]))
                tempo = false;
            answer.push_back(tempo);
        }
        return answer;
    }
};