import Models

# Z/3Z, additive
class Z(Models.Element):
    def __init__(self, val):
        self._val = val % 3
    def __add__(self, other):
        return (self._val + other._val) % 3
    def __mul__(self, val):
        return Z(self._val * val)

# Quaternions of 1, multiplicative
class Q(Models.Element):
    __vals = [1, 'i', 'j', 'k']
    __key = 0
    __sign = 1
    def __init__(self, key, sign):
        self.__key = key
        self.__sign = sign
    def __str__(self):
        sign = ""
        if (self.__sign < 0):
            sign = "-"
        return "{0}{1}".format(sign, self.__vals[self.__key])
    def __eq__(self, other):
        return ((self.__key == other.__key) and
                (self.__sign == other.__sign))
    def __lt__(self, other):
        if (self.__key < other.__key):
            return True
        elif (self.__key == other.__key):
            return (self.__sign < other.__sign)
        else:
            return False
    def __mul__(self, other):
        if (self.__key == other.__key):
            key = 0
            if (self.__key == 0):
                mult = 1
            else:
                mult = -1
        elif (self.__key == 0):
            key = other.__key
            mult = 1
        elif (other.__key == 0):
            key = self.__key
            mult = 1
        else:
            if ((self.__key + 1 == other.__key) or
                    (self.__key == 3 and other.__key == 1)):
                mult = 1
            else:
                mult = -1
            keymod = (self.__key + other.__key) % 4
            if (keymod == 0):
                key = 2
            else:
                key = keymod
        sign = self.__sign * other.__sign * mult
        return Q(key, sign)
    def Psi(self):
        if (self.__key < 2):
            return 1
        else:
            return -1

# Z/3Z*Q8
class ZQ(Models.Element):
    __z = None
    __q = None
    __s = None
    def __init__(self, z, q, s=None):
        if (s == None):
            self.__z = z
            self.__q = q
        else:
            self.__z = Z(z)
            self.__q = Q(q, s)
    def __str__(self):
        return "({0}, {1})".format(str(self.__z), str(self.__q))
    def __eq__(self, other):
        return (self.__z == other.__z) and (self.__q == other.__q)
    def __lt__(self, other):
        if (self.__z < other.__z):
            return True
        elif (self.__z == other.__z):
            return (self.__q < other.__q)
        else:
            return False
    def __mul__(self, other):
        return ZQ(Z(self.__z + other.__z * self.__q.Psi()),
                self.__q * other.__q)
    def __pow__(self, power):
        res = ZQ(0, 0, 1)
        while (power > 0):
            res *= self
            power -= 1
        return res
