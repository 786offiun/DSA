class Solution(object):
    def reverseWords(self, s):
        r=''
        word=s.split()
        for i in range(len(word)):
            tem=word[i]
            r+=tem[::-1]
            if i!=len(word)-1:
                r+=' '
            
        return r
       

       
       
        