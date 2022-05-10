/*
Submission Detail:{
    Difficulty : Medium
    Acceptance Rate : 23.61 %
    Runtime : 45 ms
    Memory Usage : 14.2 MB
    Testcase : 39 / 39 passed
    Ranking : 
        Your runtime beats 45.53 % of python3 submissions.
        Your memory usage beats 00.00 % of submissions.
}
*/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator == 0: return "0"
        neg = False
        if numerator < 0 and denominator < 0:
            numerator, denominator = map(abs,(numerator, denominator))
        elif numerator < 0 or denominator < 0:
            numerator, denominator = map(abs,(numerator, denominator))
            neg = True
        
        out = str(numerator//denominator)
        if numerator % denominator:
            out += "."
        remainders = []
        quotients = []
        numerator %= denominator
        while numerator:
            numerator *= 10
            if str(numerator) in remainders:
                duplicateStart = remainders.index(str(numerator))
                out += "".join(quotients[:duplicateStart])
                out += "("+"".join(quotients[duplicateStart:])+")"
                return "-"+out if neg else out
            else:
                remainders.append(str(numerator))
                quotients.append(str(numerator // denominator))
                numerator %= denominator
        out += "".join(quotients)
        return "-"+out if neg else out
    
    
        '''neg = True if numerator/denominator < 0 else False
        numerator = -numerator if numerator < 0 else numerator
        denominator = -denominator if denominator < 0 else denominator
        out = str(numerator//denominator)
        if numerator % denominator:
            out += "."
        remainders = []
        quotients = []
        numerator %= denominator
        while numerator:
            numerator *= 10
            if str(numerator) in remainders:
                duplicateStart = remainders.index(str(numerator))
                out += "".join(quotients[:duplicateStart])
                out += "("+"".join(quotients[duplicateStart:])+")"
                return "-"+out if neg else out
            else:
                remainders.append(str(numerator))
                quotients.append(str(numerator // denominator))
                numerator %= denominator
        out += "".join(quotients)
        return "-"+out if neg else out'''