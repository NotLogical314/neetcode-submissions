class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string , vector<string>>dict;
        std::vector<vector<string>>result;

        for (string s : strs){
            string srtd = s;
            sort(srtd.begin(), srtd.end());
            dict[srtd].push_back(s);
        }

        for (auto& pair : dict){
            result.push_back(pair.second);
        }

        return result;
    }
};
