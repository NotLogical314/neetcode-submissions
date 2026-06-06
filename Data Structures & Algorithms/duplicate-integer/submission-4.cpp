class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int>  new_nums(nums.begin(), nums.end());

        return nums.size() != new_nums.size();
    }
};