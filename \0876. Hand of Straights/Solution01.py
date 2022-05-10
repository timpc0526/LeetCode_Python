/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.18 %
    Runtime : 280 ms
    Memory Usage : 15.5 MB
    Testcase : 84 / 84 passed
    Ranking : 
        Your runtime beats 52.59 % of python3 submissions.
        Your memory usage beats 96.09 % of python3 submissions.
}
*/

class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        # 326ms ft42.41
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
                
        
                
             