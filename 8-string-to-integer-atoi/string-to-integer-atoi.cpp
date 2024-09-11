class Solution {
public:
    int myAtoi(string sorig) {
        string s;
        bool alrdig = false;
        for (char c : sorig) {
            if (alrdig && !isdigit(c)) break;
            if (isspace(c)) continue;
            if (!(isdigit(c) || c == '+' || c == '-')) break;
            s = s + c;
            alrdig = true;
        }
        int sign = s[0] == '+' ? 1 : s[0] == '-' ? -1 : 1;
        int res = 0;
        for (int i = (s[0] == '+' || s[0] == '-' ? 1 : 0); i < s.size(); i++) {
            if (res > INT_MAX / 10) return INT_MAX;
            if (res < INT_MIN / 10) return INT_MIN;
            res *= 10;
            int digit = s[i] - '0';
            if (res > INT_MAX - digit) return INT_MAX;
            if (res < INT_MIN + digit) return INT_MIN;
            res += (sign == -1 ? -digit : digit);
        }
        return res;
    }
};