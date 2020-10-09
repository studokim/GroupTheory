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
        for i in range(__self._ord):
            res += str(self[i])
            if (i < __self._ord - 1):
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
    _ord = 0
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
        index = self._members.index(g)
        if not(index in self.__invMembers):
            if (self._additive):
                for h in self:
                    if (g + h == self._neutral):
                        self.__invMembers[index] = h
            else:
                for h in self:
                    if (g * h == self._neutral):
                        self.__invMembers[index] = h
        return self.__invMembers[index]
    def IsAdditive(self):
        return self._additive

#  self.__classes is for the backwards compatibility
#  with the Group
class FactorGroup(Group):
    __classes = []
    def __init__(self, G, H):
        for g in G:
            gH = ClassSmezh(g, H)
            if not(gH.Member() in self._members):
                self._members.append(gH.Member())
                self.__classes.append(gH)
    def GetClassByMember(self, g):
        return self._members[self.__classes.index(g)]

class Commutator(Element):
    def __init__(self, group, g, h):
        if (group.IsAdditive()):
            self._val = g + h + group.Inv(g) + group.Inv(h)
        else:
            self._val = g * h * group.Inv(g) * group.Inv(h)

#  Not sure if we must sort the _members in ascending order
#  (the '<' operator in the Element and its successors is needed),
#  or just hope that the least element will be taken first.
class ClassSmezh(Enumerable):
    __subgroup = None
    def __init__(self, g, H):
        self.__subgroup = H
        self._members = []
        if (H.IsAdditive()):
            for h in H:
                self._members.append(g + h)
        else:
            for h in H:
                self._members.append(g * h)
        self._members.sort()
        self._ord = len(self._members)
    def __mul__(self, other):
        if (self.__subgroup == other.__subgroup):
            return (ClassSmezh(self.Member() * other.Member(),
                self.subgroup))
        else:
            return None
    def Member(self):
        return self.members[0]

#  We know that for all the Groups with self._ord < 96
#  the Commutant is just the set of all the Commutators.
#  Don't want to work with bigger Groups :(
class Commutant(Enumerable):
    def __init__(self, G):
        for g in G:
            c = Commutator(g)
            if not(c in self._members):
                self._members.append(c)
        self._members.sort()
        self._ord = len(self._members)
