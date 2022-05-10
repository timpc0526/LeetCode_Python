/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 35.39 %
    Runtime : 57 ms
    Memory Usage : 13.8 MB
    Testcase : 172 / 172 passed
    Ranking : 
        Your runtime beats 27.59 % of python3 submissions.
        Your memory usage beats 77.04 % of python3 submissions.
}
*/

from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result = permutations(arr)
        #print(list(result))
        hour_max = float('-inf')
        minute_max = float('-inf')
        for i in list(result):
            hour = i[0]*10+i[1]
            minute = i[2]*10+i[3]
            if hour >= 24:
                continue
            if minute >= 60:
                continue
            if hour_max < hour:
                hour_max = hour
                minute_max = minute
            elif hour_max == hour:
                minute_max = max(minute_max, minute)
        print((hour_max, minute_max))
        if hour_max == float('-inf'):
            return ""
        else:
            if hour_max < 10:
                hour_max = "0"+str(hour_max)
            if minute_max < 10:
                minute_max = "0"+str(minute_max)
            return str(hour_max)+':'+str(minute_max)
        