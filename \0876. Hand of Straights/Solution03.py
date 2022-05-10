/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.18 %
    Runtime : 334 ms
    Memory Usage : 15.4 MB
    Testcase : 84 / 84 passed
    Ranking : 
        Your runtime beats 34.00 % of python3 submissions.
        Your memory usage beats 96.09 % of python3 submissions.
}
*/

class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
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
                
        
                
             