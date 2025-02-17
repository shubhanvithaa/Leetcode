class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        str1 = ''
        str2 = ''
        len1 = len(word1)
        len2 = len(word2)
        res=''
        i =0
        j =0
        while(i<len1 and j<len2):
            res+=word1[i]
            res+=word2[j]
            i = i+1
            j = j+1
        str1 = word1[i:len1]
        str2 = word2[j:len2]
        if (i<len1):
            res+= str1
        elif(j<len2):
            res+= str2


        return res