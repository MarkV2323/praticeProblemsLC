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
    // I am going to use a two-pointers approach to solve this problem.
    //
    // Pointer 1: Will move along to find the first "val" element.
    //            Once found, the index of this element will be stored in Pointer 1.
    //
    // Pointer 2: Only moves along after Pointer 1 is found. Will move along until
    //            the first non "val" element is found. Once found, the index of this
    //            element will be stored in Pointer 2. 
    //
    //            After finding both P1 and P2, we will do a swap operation on them
    //            and reset both pointers back to nothing.
    //
    //            This will essentially move all "val" elements to the back of the
    //            nums vector
    if (nums.size() == 1) {
        if (nums[0] == val) {
            nums.empty();
            return 0;
        }
        return 1;
    }

    int p1 = -1;
    int kFound = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] == val && p1 == -1) {
            p1 = i;
        }
        if (nums[i] != val && p1 != -1) {
            cout << "Swapping " << nums[p1] << " with " << nums[i] << endl;
            int tmp = nums[p1];
            nums[p1] = nums[i];
            nums[i] = tmp;
            kFound++;
            i = p1;
            p1 = -1;
        }
    }

    if (p1 != -1) {
        nums.empty();
        return 0;
    }

    return nums.size() - kFound;
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


}
