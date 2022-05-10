/*
Submission Detail:{
    Difficulty : Easy
    Acceptance Rate : 50.58 %
    Runtime : 59 ms
    Memory Usage : 14.5 MB
    Testcase : 11 / 11 passed
    Ranking : 
        Your runtime beats 19.69 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

from itertools import combinations
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        
        #61ms ft7.79
        '''return [f'{hh}:{mm:02}' for hh in range(12) for mm in range(60)
                                if f'{hh:b}{mm:b}'.count('1') == turnedOn]'''
        
        
        #49ms ft15.05
        LED = [42, 26, 18 , 14 , 12, 11, 8, 4, 2, 1]
        num = 0
        h_sum = 0
        m_sum = 0
        out = []
        #turnedOn = 2
        #print(list(combinations(LED, turnedOn)))
        for i in list(combinations(LED, turnedOn)):
            for j in i:
                if j > 10:
                    m_sum += (j - 10)
                else:
                    h_sum += (j)
            if m_sum >= 60 or h_sum >= 12:
                h_sum = 0
                m_sum = 0
                continue
            if len(str(m_sum)) == 1:
                m_sum = '0'+str(m_sum)
            out.append(str(h_sum)+':'+str(m_sum))
            h_sum = 0
            m_sum = 0
        return out
            
            
                
                
        
        