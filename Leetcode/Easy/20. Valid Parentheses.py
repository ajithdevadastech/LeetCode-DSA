class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []

        dictSymbols = {}
        dictSymbols[')'] = '('
        dictSymbols['}'] = '{'
        dictSymbols[']'] = '['

        if s[0] in dictSymbols.keys():
            return False
        else:
            st.append(s[0])

        i = 1
        while True:

            if i  == len(s):
                if len(st) > 0:
                    return False
                else:
                    return True
            else:
                if s[i] in dictSymbols.keys():
                    if len(st) == 0:
                        st.append(s[i])
                        i=i+1
                    elif st[-1] == dictSymbols[s[i]]:
                        st.pop()
                        i = i + 1
                    else:
                        st.append(s[i])
                        i=i+1
                else:
                    st.append(s[i])
                    i=i+1