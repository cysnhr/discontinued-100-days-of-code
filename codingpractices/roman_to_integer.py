class Solution(object):
    def romanToInt(self, s):
        
        rm = ["I", "V", "X", "L", "C", "D", "M"]
        nm = [1, 5, 10, 50, 100, 500, 1000, 0]
        
        # IV
        # VI
        num_list = []
        for l in s:
            for i in range(0, len(rm)):
                if l == rm[i]:
                    num_list.append(nm[i])
                
        num_list.append(0)
        
        # answer variable
        ans=0
        for n in range(0,len(num_list)-1):
            if num_list[n] < num_list[n+1]:
                ans -= num_list[n]
            else:
                ans += num_list[n]
            
        return ans

        
        """
        :type s: str
        :rtype: int
        """
        
