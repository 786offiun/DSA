class Solution(object):
    def addBinary(self, a, b):
        c=int(a,2)
        d=int(b,2)
        e=c+d
        a=bin(e)
        return a[2:]
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        