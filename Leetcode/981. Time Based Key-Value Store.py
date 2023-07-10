from sortedcontainers import SortedDict


class TimeMap(object):

    def __init__(self):
        self.pd = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.pd.keys():
            self.pd[key] = SortedDict()

        self.pd[key][timestamp] = value

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.pd.keys():
            return ""

        if timestamp in self.pd[key].keys():
            return self.pd[key][timestamp]

        # binary search for the given timestamp.

        arr = self.pd[key].keys()

        b = 0
        e = len(arr)-1

        while b < e:
            if e-b == 1:
                if timestamp > arr[e]:
                    return self.pd[key][arr[e]]
                elif timestamp > arr[b]:
                    return self.pd[key][arr[b]]
                else:
                    return ""
            if timestamp < arr[(b + e) // 2]:
                e = (b + e) // 2
            else:
                b = (b + e) // 2

        return self.pd[key][arr[b]]

o = TimeMap()
o.set("a", "bar", 1)
o.set("x", "b", 3)
print(o.get("b", 3))
print(o.get("love", 10))
print(o.get("love", 15))
print(o.get("love", 20))
print(o.get("love", 25))