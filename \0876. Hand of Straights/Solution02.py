/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.18 %
    Runtime : 326 ms
    Memory Usage : 15.4 MB
    Testcase : 84 / 84 passed
    Ranking : 
        Your runtime beats 36.43 % of python3 submissions.
        Your memory usage beats 96.09 % of python3 submissions.
}
*/

class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        # 334ms ft40.56
        if len(hand) % gs != 0: return False
        hand = sorted(hand)
        while hand:
            initial = hand[0]
            try:
                for i in range(gs):
                    hand.remove(initial+i)
            except:
                return False
        return True
                
        
                
             