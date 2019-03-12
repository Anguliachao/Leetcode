#Python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        sorted_nums = sorted(nums)
        length = len(nums)
        for i in range(length):
            target = -sorted_nums[i]
            front,back = i+1,length-1
            while front<back:
                two_sum = sorted_nums[front]+sorted_nums[back]
                if two_sum < target:
                    front+=1
                elif two_sum > target:
                    back-=1
                else:
                    if [sorted_nums[i],sorted_nums[front],sorted_nums[back]] not in solutions:
                        solutions.append([sorted_nums[i],sorted_nums[front],sorted_nums[back]])
                    front+=1
                    back-=1
        return solutions

#C++
class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
    
    vector<vector<int> > res;

    std::sort(num.begin(), num.end());

    for (int i = 0; i < num.size(); i++) {
        
        int target = -num[i];
        int front = i + 1;
        int back = num.size() - 1;

        while (front < back) {

            int sum = num[front] + num[back];
            
            // Finding answer which start from number num[i]
            if (sum < target)
                front++;

            else if (sum > target)
                back--;

            else {
                vector<int> triplet(3, 0);
                triplet[0] = num[i];
                triplet[1] = num[front];
                triplet[2] = num[back];
                res.push_back(triplet);
                
                // Processing duplicates of Number 2
                // Rolling the front pointer to the next different number forwards
                while (front < back && num[front] == triplet[1]) front++;

                // Processing duplicates of Number 3
                // Rolling the back pointer to the next different number backwards
                while (front < back && num[back] == triplet[2]) back--;
            }
            
        }

        // Processing duplicates of Number 1
        while (i + 1 < num.size() && num[i + 1] == num[i]) 
            i++;

    }
    
    return res;
    
}
};
