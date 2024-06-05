#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

/*
 * Given a pattern and a string s, find if s follows the same pattern.
 * 
 * Here follow means a full match, such that there is a bijection between 
 * a letter in pattern and a non-empty word in s.
 *
*/
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        // Vars used
        unordered_map<string, char> uMap {};
        string tmpWord = "";
        int mapVal = 0;

        for (int i = 0; i < s.size(); i++) {
            if (!isspace(s[i])) {
                tmpWord += s[i];
                if (i != s.size() - 1) {
                    continue;
                }
            }

            if (!uMap.contains(tmpWord)) {
                for (auto& pair : uMap) {
                    if (pair.second == pattern[mapVal]) {
                        return false;
                    }
                }
                uMap[tmpWord] = pattern[mapVal];
            } else if (uMap[tmpWord] != pattern[mapVal]) {
                return false;
            } 

            mapVal++;
            tmpWord = "";
        }

        if (mapVal != pattern.size()) {
            return false;
        }

        return true;
    }
};

int main() {
    Solution s {};
    auto r = s.wordPattern("abba", "cat dog dog cat");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("jquery", "jquery");
    cout << "(J) Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("a", "cat");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("ab", "cat dog");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("aa", "cat cat");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("aa", "cat dog");
    cout << "Value Returned: " << boolalpha << r << endl;
}
