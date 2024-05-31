#include <iostream>
#include <vector>
#include <string>

using namespace std;

/*
 * Given an integer array nums and an integer val, remove all occurrences of val in
 * nums in-place. The order of the elements may be changed. Then return the number
 * of elements in nums which are not equal to val.
 *
 * Consider the number of elements in nums which are not equal to val be k,
 * to get accepted, you need to do the following things:
 *
 * Change the array nums such that the first k elements of nums contain the elements
 * which are not equal to val. The remaining elements of nums are not important as well
 * as the size of nums.
 *
 * Return k.
 */
class Solution {
public:
int removeElement(vector<int>& nums, int val) {
    // Simple cases that can be solved quickly
    if (nums.size() == 1) {
        if (nums[0] == val) {
            auto b = nums.empty();
            return 0;
        }
        return 1;
    }

    int kFound = 0;
    bool trySwap = false;

    for(int i = 0; i < nums.size(); i++) {
        // Two cases:
        // 1 - We do NOT find val -> continue
        // 2 - We do find val -> go search for a non val
        // kFound is incremented on the first case, and on swaps
        // because we will not encouter non-val after swap again
        if (nums[i] != val) {
            kFound++;
            continue;
        }
        
        trySwap = true;

        for(int j = i + 1; j < nums.size(); j++) {
            // Two cases:
            // 1 - We find another val -> continue
            // 2 - We find non-val -> swap non-val & val in place
            if (nums[j] == val) {
                continue;
            }
            // Commented out to lower Runtime ms on Leetcode
            //cout << "Swapping " << nums[i] << " with " << nums[j] << endl;
            auto tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            kFound++;
            trySwap = false;
            break;
        }

        // If trySwap is true, we never made a swap. Set these values to 0 JIC.
        if (trySwap) {
            nums[i] = 0;
        }
    }

    // Return number of non-val numbers left in nums
    return kFound;
}

};

int main() {
    vector<int> test {3, 2, 2, 3};
    int v = 3;
    Solution sol = Solution();
    int k = sol.removeElement(test, v);
    
    cout << "Returned Value: " << k << endl;
    for (auto& e : test) {
        cout << to_string(e) << endl;
    }

    // Input: nums = [0,1,2,2,3,0,4,2], val = 2
    vector<int> test2 {0, 1, 2, 2, 3, 0, 4, 2};
    v = 2;
    k = sol.removeElement(test2, v);
    
    cout << "Returned Value: " << k << endl;
    for (auto& e : test2) {
        cout << to_string(e) << endl;
    }

    // Input: nums = [3, 3], val = 3
    vector<int> test3 {3, 3};
    v = 3;
    k = sol.removeElement(test3, v);

    cout << "Returned Value: " << k << endl;
    for (auto& e : test3) {
        cout << to_string(e) << endl;
    }

}
