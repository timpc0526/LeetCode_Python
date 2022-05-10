/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 52.62 %
    Runtime : 1400 ms
    Memory Usage : 18.9 MB
    Testcase : 55 / 55 passed
    Ranking : 
        Your memory usage beats 20.90 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = collections.Counter()
        for b in words2:
            counter |= collections.Counter(b)
            print(counter)
        return [a for a in words1 if not counter - collections.Counter(a)]
        
        
        # 868ms ft77.69
        #words2 = ''.join(words2)
        '''w2 = collections.Counter()
        for b in words2:
            # |= oréç®ç¬¦ åªè¦å©èæä¸åçº1å³çº1
            w2 |= collections.Counter(b)
            print(w2)
        out = []
        for i in words1:
            w1 = collections.Counter(i)
            check = True
            for j in w2:
                if w1[j] < w2[j]:
                    check = False
                    break
            if check:
                out.append(i)
        return out'''
            