class Solution {
public:
    static const int MOD = 1e9 + 7;

    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.size();

        vector<int> prefNZ(n + 1, 0);
        vector<long long> prefSum(n + 1, 0);

        vector<int> digits;

        for (int i = 0; i < n; i++) {
            int d = s[i] - '0';
            prefNZ[i + 1] = prefNZ[i] + (d != 0);
            prefSum[i + 1] = prefSum[i] + d;
            if (d != 0) digits.push_back(d);
        }

        int m = digits.size();

        vector<long long> pow10(m + 1, 1);
        for (int i = 1; i <= m; i++)
            pow10[i] = (pow10[i - 1] * 10) % MOD;

        vector<long long> prefVal(m + 1, 0);
        for (int i = 0; i < m; i++)
            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD;

        vector<int> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int l = q[0], r = q[1];

            int L = prefNZ[l];
            int R = prefNZ[r + 1];
            int len = R - L;

            long long x = (prefVal[R] - prefVal[L] * pow10[len]) % MOD;
            if (x < 0) x += MOD;

            long long sum = prefSum[r + 1] - prefSum[l];

            ans.push_back((x * sum) % MOD);
        }

        return ans;
    }
};