#my python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(i) for i in digits]
        str_digits = ''.join(digits)
        int_digits = int(str_digits)
        int_digits+=1
        new_digits = list(str(int_digits))
        new_digits = [int(x) for x in new_digits]
        return new_digits
        
#Optimized python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if length <1:
            return [1]
        for x in reversed(range(length)):
            #for x in reversed(range(length)):
            
            
            if digits[x]+1 <10:
                digits[x]+=1
                return digits
            else:
                digits[x]=0
        digits.insert(0,1)
        return digits
        
##C++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size = digits.size();
        if( !size){
            return digits;
        }
        for(int i=size-1;i>=0;i--){
            if( digits[i]+1 >9){
                digits[i] = 0;
                if(i==0){
                    digits.insert(digits.begin(),1);
                }
            }
            else{
                digits[i]+=1;
                break;
            }
            
        }
        return digits;
    }
};
