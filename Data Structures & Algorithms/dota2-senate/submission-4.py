class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        while 'R' in senate and 'D' in senate:
            n = len(senate)

            for i in range(n):
                if senate[i] == '':
                    continue

                if senate[i] == 'R':
                    for k in range(1, n):
                        j = (i + k) % n
                        if senate[j] == 'D':
                            senate[j] = ''
                            break

                elif senate[i] == 'D':
                    for k in range(1, n):
                        j = (i + k) % n
                        if senate[j] == 'R':
                            senate[j] = ''
                            break

            senate = [x for x in senate if x != '']

        return "Radiant" if 'R' in senate else "Dire"