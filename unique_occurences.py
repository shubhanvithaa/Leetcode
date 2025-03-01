class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        arr.append('*')
        store = {}
        count = 0

        for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                count+=1
            else:
                count+=1
                store[arr[i-1]] = count
                count = 0

        lis = []
        for i in store.values():
            lis.append(i)
        lis.sort()
        for i in range(1,len(lis)):
            if (lis[i-1] == lis[i]):
                return False
        return True