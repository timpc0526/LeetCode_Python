/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 46.37 %
    Runtime : 44 ms
    Memory Usage : 14.3 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 40.84 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        
        if len(nums)==0:
            return res
        
        ans=str(nums[0])
        
        for i in range(1,len(nums)):     
            if nums[i]!=nums[i-1]+1: 
                if ans!=str(nums[i-1]):           
                    ans=ans+"->"+str(nums[i-1])
                res.append(ans)
                ans=str((nums[i]))
     
        if ans!=str(nums[-1]):
            res.append(ans+"->"+str(nums[-1]))     
        else:
            res.append(ans)
        
        return res
        
        
        '''tmp = nums[0]
        out = []
        num_len = len(nums)
        if len(nums)==0:
            return out
        for i in range(1, num_len):
            if i < num_len-1 and nums[i]+1 == nums[i+1]:
                tmp.append(nums[i])
                continue
            elif i < num_len-1 and tmp == [nums[i]]:
                out.append(str(nums[i]))
                tmp = [nums[i+1]]
            elif i < num_len-1 and nums[i]+1 < nums[i+1]:
                out.append(str(tmp[0])+"->"+str(nums[i]))
                tmp = [nums[i+1]]
        if tmp != [nums[num_len-1]]:
            tmp.append(nums[num_len-1])
        print(tmp)
        if len(tmp) == 1:
            out.append(str(nums[num_len-1]))
        else:
            out.append(str(tmp[0])+"->"+str(nums[num_len-1]))
        print(out)
        return out'''
                
                
        