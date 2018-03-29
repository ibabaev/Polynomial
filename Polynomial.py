class Polynomial:

    def __init__(self, value):
        if not isinstance(value, list):
            raise TypeError("Must be list")
        if len(value) == 0:
            raise TypeError("Should be not null")
        if not all(isinstance(c, (int, float)) for c in value):
            raise TypeError("List must contain int or float type")
        nullCondition = next((i for i, x in enumerate(value) if x != 0), None)
        self.coeffs = [0] if nullCondition == None else value[nullCondition:]

    def __str__(self):
        leng = len(self.coeffs)
        if leng == 1:
            return str(self.coeffs[0])
        res = ""
        for i in range(0, leng):
            pow = str(leng - 1 - i)
            if (self.coeffs[i] != 0):
                if (self.coeffs[i] >= 0):
                    res += "+"
                coeff =  "" if self.coeffs[i] == 1 and i != leng-1 else "-" if self.coeffs[i] == -1 else str(self.coeffs[i])
                if i == leng - 1:
                    res += coeff
                elif i == leng - 2:
                    res += coeff + "x"
                else:
                    res += coeff + "x" + pow
        if res.startswith("+"):
            res = res[1:]
        return res

    def __eq__(self, value):
        if isinstance(value, Polynomial):
            return self.coeffs == value.coeffs
        elif isinstance(value, int) or isinstance(value, float):
            return len(self.coeffs) == 1 and self.coeffs[0] == value
        else:
            raise TypeError("Polynom must be compared with other polynom or int|float constant")

    def __add__(self, value):
        if isinstance(value, Polynomial):
            res = self.add_lists(self.coeffs, value.coeffs) if len(self.coeffs) > len(value.coeffs) else self.add_lists(value.coeffs, self.coeffs)
        elif isinstance(value, int) or isinstance(value, float):
            if self.coeffs:
                res = self.coeffs[:]
                res[-1] += value
            else:
                res = value
        else:
            raise TypeError("Polynom must be computed with other polynom or int|float constant")
        return Polynomial(res)

    def __mul__(self, value):
        if isinstance(value, Polynomial):
            res = [0] * (len(self.coeffs) + len(value.coeffs) - 1)
            for i1, i2 in enumerate(self.coeffs):
                for j1, j2 in enumerate(value.coeffs):
                    res[i1 + j1] += i2 * j2
        elif isinstance(value, int) or isinstance(value, float):
            res = [i * value for i in self.coeffs]
        else:
            raise TypeError("Polynom must be computed with other polynom or int|float constant")
        return Polynomial(res)

    def __radd__(self, value):
        return self + value

    def __rmul__(self, value):
        return self * value

    def __sub__(self, value):
        return self.__add__(-value)

    def __neg__(self):
        return Polynomial([-x for x in self.coeffs])

    def add_lists(self, l1, l2):
            return [i2 + l2[len(l2) - len(l1) + i1] if i1 >= len(l1) - len(l2) else i2 for i1, i2 in enumerate(l1)]