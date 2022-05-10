/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 46.37 %
    Runtime : 59 ms
    Memory Usage : 14.3 MB
    Testcase : 28 / 28 passed
    Ranking : 
        Your runtime beats 10.60 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        # 42ms ft12.7
        '''res=[]
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
        
        return res'''
        
        ranges = []
        if not nums:
            return ranges
        ranges = [[nums[0],nums[0]]]
        for i in nums[1:]:

            if i - ranges[-1][1]==1:
                ranges[-1][1] = i
                print(ranges)
            else:
                ranges.append([i,i])
                print(ranges)
        for i in range(len(ranges)):
            if ranges[i][0]==ranges[i][1]:
                ranges[i].pop()
                ranges[i] = "{}".format(ranges[i][0])
            else:
                ranges[i] = "{}->{}".format(ranges[i][0],ranges[i][1])
        return ranges
        
        
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
                
                
        