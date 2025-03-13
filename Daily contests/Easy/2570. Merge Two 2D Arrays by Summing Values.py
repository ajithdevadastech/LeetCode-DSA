class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """

        i = 0
        j = 0
        r = []

        while True:
            if nums1[i][0] == nums2[j][0]:
                r.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i = i + 1
                j = j + 1
            elif nums1[i][0] < nums2[j][0]:
                r.append([nums1[i][0], nums1[i][1]])
                i = i + 1
            else:
                r.append([nums2[j][0], nums2[j][1]])
                j = j + 1

            if i > len(nums1)-1:
                if j <= len(nums2) - 1:
                    r = r + nums2[j:]
                break
            if j > len(nums2)-1:
                if i <= len(nums1) - 1:
                    r = r + nums1[i:]
                break

        return r

o = Solution()
nums1 = [[148,597],[165,623],[306,359],[349,566],[403,646],[420,381],[566,543],[730,209],[757,875],[788,208],[932,695]]
nums2 = [[74,669],[87,399],[89,165],[99,749],[122,401],[138,16],[144,714],[148,206],[177,948],[211,653],[285,775],[309,289],
         [349,396],[386,831],[403,318],[405,119],[420,153],[468,433],
         [504,101],[566,128],[603,688],[618,628],[622,586],[641,46],[653,922],[672,772],[691,823],[693,900],
         [756,878],[757,952],[770,795],[806,118],[813,88],[919,501],[935,253],[982,385]]
print(o.mergeArrays(nums1,nums2))





