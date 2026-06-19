class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map< string , vector<string>> dict;
        std::vector <vector <string>> result;

        for (string c : strs){
            string key = c;
            sort(key.begin(), key.end());
            dict[key].push_back(c);
        }

        for (auto& pair: dict){
            result.push_back(pair.second);
        }
        return result;
    }
};
