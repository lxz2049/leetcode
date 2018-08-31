/*
 * [745] Find Smallest Letter Greater Than Target
 *
 * https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
 *
 * algorithms
 * Easy (44.49%)
 * Total Accepted:    22.9K
 * Total Submissions: 53.3K
 * Testcase Example:  '["c","f","j"]\n"a"'
 *
 * 
 * Given a list of sorted characters letters containing only lowercase letters,
 * and given a target letter target, find the smallest element in the list that
 * is larger than the given target.
 * 
 * Letters also wrap around.  For example, if the target is target = 'z' and
 * letters = ['a', 'b'], the answer is 'a'.
 * 
 * 
 * Examples:
 * 
 * Input:
 * letters = ["c", "f", "j"]
 * target = "a"
 * Output: "c"
 * 
 * Input:
 * letters = ["c", "f", "j"]
 * target = "c"
 * Output: "f"
 * 
 * Input:
 * letters = ["c", "f", "j"]
 * target = "d"
 * Output: "f"
 * 
 * Input:
 * letters = ["c", "f", "j"]
 * target = "g"
 * Output: "j"
 * 
 * Input:
 * letters = ["c", "f", "j"]
 * target = "j"
 * Output: "c"
 * 
 * Input:
 * letters = ["c", "f", "j"]
 * target = "k"
 * Output: "c"
 * 
 * 
 * 
 * Note:
 * 
 * letters has a length in range [2, 10000].
 * letters consists of lowercase letters, and contains at least 2 unique
 * letters.
 * target is a lowercase letter.
 * 
 * 
 */
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        char ans = 0;
        int min_distance = 26;
        for (int i=0; i<letters.size(); ++i) {
            int distance = (letters[i] - target + 26) % 26;
            if (distance > 0 && distance < min_distance) {
                min_distance = distance;
                ans = letters[i];
            }
        }       
        return ans;
    }

    void test() {
        char arr[] = {'c', 'f', 'j'};
        vector<char> letters(arr, arr+3);
        char ans = nextGreatestLetter(letters, 'g'); cout<<ans<<endl;
        ans = nextGreatestLetter(letters, 'j'); cout<<ans<<endl;
        ans = nextGreatestLetter(letters, 'k'); cout<<ans<<endl;
    }
};
