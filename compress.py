class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        length = len(chars)
        if len(chars) == 1:
            return 1
        else:
            count = 0
            res = []
            chars.append('*')
            for i in range(1,len(chars)):
                if chars[i-1] == chars[i]:
                    count+=1

                else:
                    count+=1
                    if(count == 1):

                        res.append(chars[i-1])
                    else:
                        res.append(chars[i-1])
                        res.append(str(count))
                    count = 0
        strs = ''.join(map(str,res))
        del chars [:]
        for i in strs:
            chars.append(i)
        j =0

        
        print(chars)

        return len(chars)
        
        