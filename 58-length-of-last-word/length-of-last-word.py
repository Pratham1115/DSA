class Solution:
    def lengthOfLastWord(self, s):
        self.s=s
        l=s.split()
        count=0
        if " " in l[-1]:
            for i in l[-2]:
                count+=1
        else :
            for i in l[-1]:
                count+=1 
        return count
        