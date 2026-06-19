class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!= t.size()){
            return false;
        }
        
        std::unordered_map<char, int>dict;

        for (char c : s) {
            dict[c]++;
        }

        for (char c : t){
            dict[c]--;
        }

        for (auto& pair : dict){
            if (pair.second == 0){
                return true;
            }
            return false;
        }
    }
};
