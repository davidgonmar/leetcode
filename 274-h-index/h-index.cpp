class Solution {
public:
    int hIndex(std::vector<int>& citations) {
        std::sort(citations.begin(), citations.end(), std::greater<int>());
        
        int n = citations.size();
        for (int i = 0; i < n; ++i) {
            if (citations[i] <= i) {
                return i;
            }
        }
        
        return n;
    }
};