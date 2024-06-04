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
        unordered_map<char, string> uMap {};
        string tmpWord = "";
        int mapVal = 0;

        for (int i = 0; i < s.size(); i++) {
            if (!isspace(s[i])) {
                tmpWord += s[i];
                if (i != s.size() - 1) {
                    continue;
                }
            }
            cout << tmpWord << endl;
            // 1 - Check if key already belongs in hashMap
            // 1a - F -> Add mapping, increment mapVal
            // 2b - T -> Get tmpWord key, compare against pattern[MapVal]
            //           T -> continue
            //           F -> return false

            // key -> pattern[mapVal]
            // val -> tmpWord 
            if (!uMap.contains(pattern[mapVal])) {
                uMap[pattern[mapVal]] = tmpWord;
            } else {
                cout << uMap[pattern[mapVal]] << " vs " << tmpWord << endl;
                if (uMap[pattern[mapVal]] == tmpWord) {
                    mapVal++;
                    continue;
                } else {
                    return false;
                }
            }
            mapVal++;
            tmpWord = "";
        }
        cout << endl;
        return true;
    }
};

int main() {
    Solution s {};
    auto r = s.wordPattern("abba", "cat dog dog cat");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("a", "cat");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("ab", "cat dog");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("aa", "cat cat");
    cout << "Value Returned: " << boolalpha << r << endl;

    r = s.wordPattern("aa", "cat dog");
    cout << "Value Returned: " << boolalpha << r << endl;
}
