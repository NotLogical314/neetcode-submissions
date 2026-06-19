class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> nums2(nums.begin(), nums.end());
        return  nums.size() != nums2.size();
    }
};