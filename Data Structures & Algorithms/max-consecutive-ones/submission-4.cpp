class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ones = 0;
        int result = 0;
        for (int num: nums){
            if (num == 1){
                ones += 1;
            }
            else {
                result = max(ones, result);
                ones = 0;
            }
        }
        return max(ones, result);
    }
};