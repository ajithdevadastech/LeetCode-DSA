class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        # reference: https://www.youtube.com/watch?v=Ua0GhsJSlWM&t=849s

        #create a m*n matrix

        if len(text1) <= len(text2):
            m = len(text1)
            n = len(text2)
        else:
            m = len(text2)
            n = len(text1)
            k = text1
            text1 = text2
            text2 = k

        arr = []

        for i in range(m):
            arr.append([0]*n)

        #start filling the matrix

        i = m-1
        while i >= 0:
            j = n-1
            while j >= 0:
                C = None
                R = None
                D = None
                if i+1 > m-1 and j+1 > n-1:
                    C = 0
                    D = 0
                    R = 0
                elif i+1 > m-1 and j+1 <= n-1:
                    D = 0
                    C = 0
                    R = arr[i][j+1]
                elif i+1 <= m-1 and j+1 > n-1:
                    R = 0
                    C = 0
                    D = arr[i+1][j]
                else:
                    C = arr[i+1][j+1]
                    D = arr[i+1][j]
                    R = arr[i][j+1]
                if text1[i] == text2[j]:
                    arr[i][j] = C+1
                else:
                    arr[i][j] = max(R,D)
                j = j - 1
            i = i - 1

        return arr[0][0]
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        """
        len(word1) + len(word2) - 2 * longest common subsequence
        """

        return len(word1) + len(word2) - 2 * self.longestCommonSubsequence(word1, word2)


o = Solution()
word1 = "leetcode"
word2 = "etco"
print(o.longestCommonSubsequence(word1,word2))



