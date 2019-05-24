#my Python solution
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        aList = list(map(int,a))
        bList = list(map(int,b))
        
        aLen = len(aList)
        bLen = len(bList)
        
        if aLen>bLen:
            longLen = aLen
            shortLen = bLen
            longList = aList
            shortList = bList
        else:
            longLen = bLen
            shortLen = aLen
            longList = bList
            shortList = aList
        
        diff = longLen-shortLen
            
        sumList = []    
        res = 0
        for i in range(longLen-1,-1,-1):
            if i<diff:
                b= 0
            else:
                b = shortList[i-diff]
            #print(i,b,summ)
            a = longList[i]
            summ = a+b+res
            sumList = [summ%2]+sumList
            if summ>1:
                res=1
                if i==0:
                    sumList.insert(0,1)
            else:
                res=0
            print(sumList)
        sumString = ''.join(list(map(str,sumList)))
        return sumString
        
#Optimized python solution
#https://leetcode.com/problems/add-binary/discuss/24500/An-accepted-concise-Python-recursive-solution-10-lines
#add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
   class Solution:
        def addBinary(self, a, b):
            if len(a)==0: return b
            if len(b)==0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'
