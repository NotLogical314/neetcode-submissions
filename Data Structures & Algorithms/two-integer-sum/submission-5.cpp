class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> new_map;

        for (int i = 0; i < nums.size(); i++){
            int needed = target - nums[i];
            if (new_map.find(needed) != new_map.end()){
                return {new_map[needed], i};
            }

            new_map[nums[i]] = i;
        }
    }
};
