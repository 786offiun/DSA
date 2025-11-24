class Solution(object):
    def strStr(self, haystack, needle):
     for i in range(len(haystack)-len(needle)+1):
          if needle==haystack[i:len(needle)+i]:
            return i
                   
          
     return -1
                    

        