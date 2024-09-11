class Solution {
public:
    unordered_map<string, bool> memo;
    
    bool isMatch(string s, string p) {
        string key = s + "____" + p;
        if (memo.find(key) != memo.end()) {
            return memo[key];
        }

        auto isCharOrDot = [](const char &s) -> bool {
            return (s == '.') || isalpha(s);
        };

        auto matchChar = [](const char &c1, const char &c2) -> bool {
            return c1 == '.' || c2 == c1;
        };
        
        bool ret = false;

        if ((p.size() >= 2) && isCharOrDot(p.at(0)) && (p.at(1) == '*')) {
            char toMatch = p.at(0);
            int spos = 0;
            string newP = p.substr(2);
            while (((spos < s.size()) && matchChar(toMatch, s.at(spos))) || spos == s.size()) {
                string newS = s.substr(spos);
                if (this->isMatch(newS, newP)) { 
                    ret = true; 
                    break; 
                }
                spos++;
            }
            ret = ret || (this->isMatch(s, newP)) || (spos < s.size() ? this->isMatch(s.substr(spos), newP) : false);
        } else if ((0 < s.size()) && (0 < p.size()) && matchChar(p.at(0), s.at(0))) {
            ret = (this->isMatch(s.substr(1), p.substr(1)));
        } else if (s == "" && p == "") {
            ret = true;
        } else {
            ret = false;
        }
        
        memo[key] = ret;
        return ret;
    }
};
