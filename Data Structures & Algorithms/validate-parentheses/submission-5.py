class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ins = ["(", "[", "{"]
        outs = [")", "]", "}"]
        dct = dict(zip(outs, ins))
        opens = []
        closes = []
        for elem in s:
            if elem in ins:
                opens.append(elem)
            if elem in outs:
                if len(opens) == 0:
                    return False
                if opens[-1] != dct[elem]:
                    return False
                opens.pop()
        if len(opens) > 0:
            return False
        return True
        