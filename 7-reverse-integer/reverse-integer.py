class Solution(object):
    
    def reverse(self, x):
        last=0
        flag=True
        if x<0:
            x=abs(x)
            flag=False

        while x>0:
            n=x%10
            last=last*10+n
            x=x//10
        if flag==0:
            last=-1*last
        if last >= -2147483648 and last <= 2147483647:
            return last
        else:
            return 0




                 
        