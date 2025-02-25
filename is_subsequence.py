class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
   

        point_s = 0
        point_t = 0
        count = 0
        while(point_s < len(s) and point_t < len(t)):
            if t[point_t] == s[point_s]:
                count+=1
                point_t+=1
                point_s+=1
            else:
                point_t+=1

        if count==len(s):
            return True
        else:
            return False