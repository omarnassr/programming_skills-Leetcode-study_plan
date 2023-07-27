class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        collective = list()

        for let in t:
            collective.append(let)

        if str(s) == '':
            print(t)
        else:
            for let in s:
                collective.remove(let)

    


        result = ''.join(collective)
        return result