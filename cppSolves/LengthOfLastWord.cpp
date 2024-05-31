#include <iostream>

using namespace std;

/*
 * Given a string s consisting of words and spaces, return the length of the last word
 * in the string
 *
 * A word is a maximal substring consisting of non-space characters only.
*/

class Solution {
public:
    int lengthOfLastWord(string s) {
        int lastWord = 0;
        int currentWord = 0;
        int i = 0;
        for (auto& c : s) {
            if (!isspace(c)) {
                currentWord++;
            }
            if (currentWord > 0 && isspace(c)) {
                lastWord = currentWord;
                currentWord = 0;
            }
            if (currentWord != 0 && i == s.size() - 1) {
                lastWord = currentWord;
                currentWord = 0;
            }
            i++;
        }

        return lastWord;
    }
};

int main() {
    Solution sol {};

    // Test Case 1
    string s = "Hello World";
    int rVal = sol.lengthOfLastWord(s);
    cout << "s: " << s << "\n" << "rVal: " << rVal << endl;

    // Test Case 2
    s = "  fly me  to  the moon";
    rVal = sol.lengthOfLastWord(s);
    cout << "s: " << s << "\n" << "rVal: " << rVal << endl;

    // Test Case 3
    s = "luffy is still joyboy";
    rVal = sol.lengthOfLastWord(s);
    cout << "s: " << s << "\n" << "rVal: " << rVal << endl;


    return 0;
}
