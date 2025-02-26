class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len_1 = len(str1)
        len_2 = len(str2)
        large = ''
        small = ''
        if len_1>len_2:
            small = str2
            large = str1
        else:
            large = str2
            small = str1
    
        list_1 = []
        list_2 = []
        max = 1

        for i in range(1,len_1):
            if len_1%i == 0:
                list_1.append(int(len_1/i))
        for i in range(1,len_2):
            if len_2%i == 0:
                list_2.append(int(len_2/i))
    
    
        if len(list_1) > len(list_2):
            for i in range(len(list_1)):
                if list_1[i] in list_2:
                    if list_1[i] > max:
                        max = list_1[i]
        else:
            for i in range(len(list_2)):
                if list_2[i] in list_1:
                    if list_2[i] > max:
                        max = list_2[i]
        tail = str1[:max]
        div1 = int(len(large)/max)
        div2 = int(len(small)/max)
        if (tail*div1 == large and tail*div2 == small):
            return tail
        else:
            return ''
        