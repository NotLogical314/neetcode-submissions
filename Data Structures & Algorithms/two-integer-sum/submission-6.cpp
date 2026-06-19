class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int , int>dict;

        for(int i = 0; i < nums.size(); i++){
            int want = target - nums[i];

            if (dict.find(want) != dict.end())
            {
                return {dict[want], i};
            }
            dict[nums[i]] = i;
        }
    }
};
