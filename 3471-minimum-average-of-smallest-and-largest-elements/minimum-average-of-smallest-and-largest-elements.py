class Solution(object):
    def minimumAverage(self, nums):
        minval=0
        maxval=0
        averages=[]
        if len(nums)==0:
            return averages
        else:
            counter=len(nums)
            while counter>0:
                maxval=max(nums)
                minval=min(nums)
                avg=(minval+maxval)/2.0
                averages.append(avg)
                nums.remove(minval)
                nums.remove(maxval)
                counter-=2
        return min(averages)


        

     
     
        