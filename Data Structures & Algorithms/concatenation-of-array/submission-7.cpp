class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> result = nums;
        result.insert(result.end(), nums.begin(), nums.end());
        return result;
   }
};