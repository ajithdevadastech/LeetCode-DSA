class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        """
        find lcs of both strings
        perform logic to find the super sequence
        """

        def longestcommonsubsequence(str1, str2):
            """
            :param str1:
            :param str2:
            :return:

            form a m+1 X n+1 DP matrix and find the lcs length and lcs
            return lcs

            refer: https://www.youtube.com/watch?v=LAKWWDX3sGw&t=0s

            """

            # for a m+1 X n+1 DP matrix and initialize to 0

            m = len(str1)
            n = len(str2)

            arr = []
            for i in range(m+1):
                k = []
                for j in range(n+1):
                    k.append(0)
                arr.append(k)

            #populate the DP matrix

            for i in range(1,m+1):
                for j in range(1,n+1):
                    if str1[i-1] == str2[j-1]:
                        arr[i][j] = arr[i-1][j-1] + 1
                    else:
                        arr[i][j] = max(arr[i-1][j], arr[i][j-1])

            # calculate longest common substring

            i = m
            j = n
            lcs = ''
            while True:
                if arr[i-1][j-1] == arr[i][j-1] and arr[i-1][j-1] == arr[i-1][j]:
                    if arr[i-1][j-1] < arr[i][j]:
                        i = i - 1
                        j = j - 1
                        lcs = str1[i] + lcs
                    else:
                        j = j - 1
                elif arr[i-1][j-1] > arr[i][j-1] and arr[i-1][j-1] > arr[i-1][j] and arr[i-1][j-1] < arr[i][j]:
                    i = i - 1
                    j = j - 1
                    lcs = str1[i] + lcs
                elif arr[i][j-1] > arr[i-1][j]:
                    j = j - 1
                else:
                    i = i - 1

                if i < 0 or j < 0:
                    break

            return lcs



        #logic to find the super sequence

        #refer: https://www.youtube.com/watch?v=pHXntFeu6f8&t=1250s

        lcs = longestcommonsubsequence(str1, str2)
        scs = ''
        p1 = 0 #str1 pointer
        p2 = 0 #str2 pointer
        p3 = 0 #lcs pointer

        flag = 1
        while True:
            if flag == 1:
                while True:
                    if str1[p1] != lcs[p3]:
                        scs = scs + str1[p1]
                        p1 = p1 + 1
                    else:
                        flag = 0
                        p1 = p1 + 1
                        break
            else:
                while True:
                    if str2[p2] != lcs[p3]:
                        scs = scs + str2[p2]
                        p2 = p2 + 1
                    else:
                        flag = 1
                        scs = scs + str2[p2]
                        p2 = p2 + 1
                        p3 = p3 + 1
                        break

            if p3 == len(lcs):
                for i in range(p1, len(str1)):
                    scs = scs + str1[i]
                for j in range(p2, len(str2)):
                    scs = scs + str2[j]
                break

        return scs

o = Solution()
str1 = 'abac'
str2 = 'cab'
print(o.shortestCommonSupersequence(str1, str2))







