//C++ solution
class Solution {
public:
    /**
     * @param str: a string
     * @return: return a string
     */
    string reverseWords(string &str) {
        
        // write your code here
        if( str.size()==0) return "";
        reverse(str,0,str.size()-1);
        int count = 0;
        for(int i =0;i<str.size();i++){
            if(str[i] == ' '){
                reverse(str,count,i-1);
                count = i+1;
            }
        }
        reverse(str,count,str.size()-1);
        return str;
    }
       
    void reverse(string &s, int begin, int end){
        while(begin<end){
            char tmp = s[begin];
            s[begin] = s[end];
            s[end] = tmp;
            begin++;
            end--;
        }
    }
};

/*
 *https://www.cnblogs.com/EdwardLiu/p/4306561.html
 *http://tiancao.me/Leetcode-Unlocked/LeetCode%20Locked/c1.html
 */
