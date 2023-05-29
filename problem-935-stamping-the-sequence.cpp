// trying to check if the performance stats are per language or not
// the exact port of the python solution
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        int n = target.length();
        int k = stamp.length();

        vector<bool> matched(n, false);

        vector<int> result;
        int matchedCount = 0;

        while (matchedCount != n) {
            bool progressed = false;

            for (int offset = 0; offset <= n - k; offset++) {
                // std::cout << offset << std::endl;
                bool isMatch = true;
                int newMatches = 0;

                for (int idx = 0; idx < k; idx++) {
                    if (stamp[idx] != target[offset + idx] && !matched[offset + idx]) {
                        isMatch = false;
                        break;
                    }

                    if (matched[offset + idx] != true) {
                        newMatches += 1;
                    }
                }

                if (newMatches != 0 && isMatch)
                {
                    for (int idx = 0; idx < k; idx++) {
                        matched[idx + offset] = true;
                    }
                    matchedCount += newMatches;
                    result.push_back(offset);
                    progressed = true;
                    break;
                }
            }

            if (!progressed && matchedCount != n) {
                result = vector<int>();
                // std::cout << "boom" << " " << matchedCount;
                break;
            }
        }

        reverse(result.begin(), result.end());

        return result;
    }
};

template <typename T, typename A>
void printVector(vector<T, A> const &vector)
{
    std::cout << "[ ";
    for (auto x: vector) {
        std::cout << x << " ";
    }
    std::cout << "]" << std::endl;
}

int main() {
    Solution x;

    printVector(x.movesToStamp("abc", "ababc"));

    return 0;
}