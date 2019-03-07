##C++ version

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        
        map<int,int> m;
        vector<int> out;
        
        for(int i : nums1) m[i]++;
        for(int j : nums2) {
            if (m[j] > 0) {
            m[j]--;
            out.push_back(j);
            }
        }
        return out;
    }

    
};

##python version
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for x in nums1:
            if x in nums2:
                result.append(x)
                nums2.remove(x)
        return result
