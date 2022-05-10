/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 44.46 %
    Runtime : 965 ms
    Memory Usage : 37.8 MB
    Testcase : 36 / 36 passed
    Ranking : 
        Your runtime beats 31.75 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

import numpy
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidate, debit, credit = None, 0, 0
	
        for i in range(len(gas)):
            credit += gas[i] - cost[i]
            if credit < 0:
                candidate, debit, credit = None, debit - credit, 0
            elif candidate is None: 
                candidate = i

        return candidate if credit >= debit else -1
        
        
        '''glen = len(gas)
        gas, cost = gas*3, cost*3
        #print(gas)
        out = []
        temp = 0
        for i in range(glen):
            for j in range(glen+1):
                if temp == 0:
                    temp = gas[i+j]
                    print(temp)
                else:
                    temp -= cost[i+j-1]
                    if temp <= 0:
                        break
                    print(temp)
                    temp += gas[i+j]
                    print(temp)
            print("---") 
            out.append(temp)
            temp = 0
        print(out)
        final = []
        for i in range(glen):
            if out[i]>0:
                return i
        return -1'''
            
        