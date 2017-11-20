def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_divide = [i for i in range(left,right+1) if '0' not in str(i) and all(i%int(m) == 0 for m in str(i))]
        return self_divide
 