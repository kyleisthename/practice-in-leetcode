def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        verti = 0
        hori = 0
        dict_V = {'U':1,'D':-1,'L':0,'R':0}
        dict_H = {'U':0,'D':0,'L':1,'R':-1}
        for i in moves:
            verti += dict_V[i]
            hori += dict_H[i]
        return not bool(verti or hori)