class Solution:
    def isValid(self, s):
        l = []

        for i in s:
            if i in "([{":
                l.append(i)
            else:
                if not l:
                    return False

                if i == ")" and l[-1] == "(":
                    l.pop()
                elif i == "]" and l[-1] == "[":
                    l.pop()
                elif i == "}" and l[-1] == "{":
                    l.pop()
                else:
                    return False

        return l == []