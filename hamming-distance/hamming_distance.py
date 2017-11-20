def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        Distance = 0
        while (x != 0 or y != 0):
            x_res = x%2
            x = x/2
            y_res = y%2
            y = y/2
            if (x_res!=y_res):
                Distance += 1
            else:
                pass
            
        return Distance