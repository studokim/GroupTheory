class Element:
    _val = None
    def __init__(self, val):
        self._val = val
    def __str__(self):
        return str(self._val)
    def __eq__(self, other):
        return (self._val == other._val)
    def __lt__(self, other):
        return (self._val < other._val)

class Enumerable:
    _members = []
    _ord = 0
    def __init__(self, lis):
        self._members = sorted(lis)
        self._ord = len(self._members)
    def __str__(self):
        res = "["
        for i in range(self._ord):
            res += str(self[i])
            if (i < self._ord - 1):
                res += ", "
        res += "]"
        return res
    def __getitem__(self, i):
        return self._members[i]
    def __iter__(self):
        self.__ptr = 0
        return self
    def __next__(self):
        if self.__ptr == self._ord:
           raise StopIteration
        member = self[self.__ptr]
        self.__ptr += 1
        return member
    def __eq__(self, other):
        return (self._members == other._members)

#  We believe that the List passed into the Constructor is really a group,
#  since we can't automatically find the inverse element.
class Group(Enumerable):
    _members = []
    __invMembers = None
    _additive = False
    _neutral = None
    def __init__(self, lis, additive = False):
        self._members = sorted(lis)
        self._ord = len(self._members)
        self._additive = additive
        self._neutral = self.Neutral()
    def __str__(self):
        res = "{"
        for i in range(self._ord):
            res += str(self[i])
            if (i < self._ord - 1):
                res += ", "
        res += "}"
        return res
    def __eq__(self, other):
        return (self._members == other._members)
    def Add(self, member):
        if not(member in self._members):
            index = 0
            while (member > self[index]):
                index += 1
            self._members.insert(index, member)
            self._ord += 1
    def Neutral(self):
        if (self._neutral is None):
            for g in self:
                for h in self:
                    if (self._additive):
                        if (g + h == g):
                            return h
                    else:
                        if (g * h == g):
                            return h
        return self._neutral
    def Ord(self):
        return self._ord
    def Inv(self, g):
        if (self.__invMembers == None):
            self.__invMembers = {}
        ig = self._members.index(g)
        if not(ig in self.__invMembers):
            for ih in range(self._ord):
                h = self._members[ih]
                if (self._additive):
                    if (g + h == self._neutral):
                        self.__invMembers[ig] = h
                else:
                    if (g * h == self._neutral):
                        self.__invMembers[ig] = h
        return self.__invMembers[ig]
    def IsAdditive(self):
        return self._additive

#  self.__classes is for the backwards compatibility
#  with the Group. Commutativity is assumpted.
class FactorGroup(Group):
    __classes = []
    def __init__(self, G, H):
        for ig in range(G.Ord()):
            g = G[ig]
            gH = ClassSmezh(g, H)
            if not(gH.Member() in self._members):
                self._members.append(gH.Member())
                self.__classes.append(gH)
        self._members.sort()
        self._neutral = self.Neutral()
        self._ord = len(self._members)
    def __str__(self):
        res = "{"
        for i in range(self._ord):
            if (i > 0):
                res += ' '
            res += str(self.__classes[i])
            if (i < self._ord - 1):
                res += ", \n"
        res += "}"
        return res
    def GetClassByMember(self, g):
        return self.__classes[self._members.index(g)]

#  Not sure if we must sort the _members in ascending order
#  (the '<' operator in the Element and its successors is needed),
#  or just hope that the least element will be taken first.
class ClassSmezh(Enumerable):
    __subgroup = None
    __left = None
    def __init__(self, g, H, left = True):
        self.__subgroup = H
        self._members = []
        self.__left = left
        if (H.IsAdditive()):
            for ih in range(H.Ord()):
                h = H[ih]
                if (self.__left):
                    self._members.append(g + h)
                else:
                    self._members.append(h + g)
        else:
            for ih in range(H.Ord()):
                h = H[ih]
                if (self.__left):
                    self._members.append(g * h)
                else:
                    self._members.append(h * g)
        self._members.sort()
        self._ord = len(self._members)
    def __mul__(self, other):
        if (self.__subgroup == other.__subgroup):
            return (ClassSmezh(self.Member() * other.Member(),
                self.subgroup))
        else:
            return None
    def Member(self):
        return self._members[0]

class Commutator(Element):
    def __init__(self, G, g, h):
        if (G.IsAdditive()):
            self._val = g + h + G.Inv(g) + G.Inv(h)
        else:
            self._val = g * h * G.Inv(g) * G.Inv(h)

#  We know that for all the Groups with self._ord < 96
#  the Commutant is just the set of all the Commutators.
#  Don't want to work with bigger Groups :(
class Commutant(Enumerable):
    def __init__(self, G):
        for ig in range(G.Ord()):
            g = G[ig]
            for ih in range(G.Ord()):
                h = G[ih]
                c = Commutator(G, g, h)
                if not(c in self._members):
                    self._members.append(c)
        self._members.sort()
        self._ord = len(self._members)
