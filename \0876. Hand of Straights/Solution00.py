/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 56.18 %
    Runtime : 282 ms
    Memory Usage : 15.7 MB
    Testcase : 84 / 84 passed
    Ranking : 
        Your runtime beats 51.64 % of python3 submissions.
        Your memory usage beats 75.40 % of python3 submissions.
}
*/

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        queue = collections.deque()
        prev, opened = -1, 0
        for card in sorted(counter):
            if opened > counter[card] or (opened > 0 and card > prev + 1):
                return False
            queue.append(counter[card] - opened)
            prev, opened = card, counter[card]
            if len(queue) == W: opened -= queue.popleft()
        return opened == 0
        
        # 280ms ft59.33
        '''if len(hand) % gs != 0: return False
        hand = sorted(hand)
        while hand:
            initial = hand[0]
            try:
                for i in range(gs):
                    hand.remove(initial+i)
            except:
                return False
        return True'''
                
        
                
             