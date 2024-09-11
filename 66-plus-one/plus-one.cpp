class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int v = digits[digits.size() - 1] + 1;
        int carry =  v / 10;
        digits[digits.size() - 1] = v % 10;
        for (auto d = digits.rbegin() + 1; d != digits.rend(); ++d) {
            int plusOne = *d + carry;
            carry = plusOne / 10;
            *d = plusOne % 10;
        }
        if (carry != 0) digits.insert(digits.begin(), carry);
        return digits;
    }
};