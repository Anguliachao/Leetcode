class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    refer: https://www.cnblogs.com/lightwindy/p/8606871.html
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        lens = len(s)
        lent = len(t)
        if abs(lens-lent)>1:
            return False
        for i in range(min(lens,lent)):
            print(s[i],t[i],i)
            if s[i]!=t[i]:
                if lens==lent:
                    return s[i+1:] == t[i+1:]
                elif lens<lent:
                    return s[i:]==t[i+1:]
                else:
                    return s[i+1:]==t[i:]
        return abs(lens-lent)==1
                
