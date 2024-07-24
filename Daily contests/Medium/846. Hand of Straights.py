import heapq
class Solution(object):
    def isNStraightHand(self, hand, groupSize):

        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False

        #create dict
        dictFreq = {}
        for h in hand:
            if h not in dictFreq.keys():
                dictFreq[h] = 1
            else:
                dictFreq[h] += 1
        #create heap
        uniqueHand = list(dictFreq.keys())
        l = len(uniqueHand)
        heapq.heapify(uniqueHand)

        i = 0
        while i < l:

            k = heapq.heappop(uniqueHand)

            if dictFreq[k] > 0:
                while dictFreq[k] > 0:
                    dictFreq[k] -= 1
                    j = 1
                    while j < groupSize:
                        if k+j not in dictFreq.keys():
                            return False
                        else:
                            if dictFreq[k+j] == 0:
                                return False
                            else:
                                dictFreq[k + j] -= 1
                        j = j + 1
            i += 1

        return True


hand = [1,1,2,2,3,3]
groupSize = 3

o = Solution()
print(o.isNStraightHand(hand, groupSize))
