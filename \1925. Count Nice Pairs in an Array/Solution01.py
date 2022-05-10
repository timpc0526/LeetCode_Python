/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 40.35 %
    Runtime : 1087 ms
    Memory Usage : 24.7 MB
    Testcase : 84 / 84 passed
    Ranking : 
        Your runtime beats 39.00 % of python3 submissions.
        Your memory usage beats 13.78 % of python3 submissions.
}
*/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        counter = collections.Counter()
        ans, mod = 0, 10**9 + 7
        rev = lambda x: int(str(x)[::-1])
        for i, num in enumerate(nums):
            key = num - rev(num)
            ans = (ans + counter[key]) % mod
            counter[key] += 1
        return ans
        
        
        
        # Time Limit Exceeded
        '''nlen = len(nums)
        rev_list = list(map(self.rev, nums))
        out = 0
        modulo = 10**9 + 7
        dic = collections.defaultdict(list)
        for i in range(nlen):
            for j in range(nlen):
                if i == j or dic[i] == j:
                    continue
                elif nums[i]+ rev_list[j] == nums[j]+rev_list[i]:
                    dic[j].append(i)
                    #print(nums[i], rev_list[j])
                    #print(nums[j], rev_list[i])
                    out+=1
        
        return (out//2)%modulo
                
    def rev(self, n):
        return int(str(n)[::-1])'''