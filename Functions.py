import Models
import MyGroup

#  Fill the G=Z/3Z*Q8 group
def MakeMyGroup():
    lis = []
    for z in range(3):
        for q in range(4):
            for s in range(-1, 2, 2):
                lis.append(MyGroup.ZQ(z, q, s))
    return Models.Group(lis)

#  Calculate orders of the G group members
def PrintOrders(G):
    e = G.Neutral()
    k1 = len(str(e)) + 1
    for g in G:
        power = 1
        while not (g ** power == e):
            power += 1
        k2 = power // 10 + 1
        print("ord {0:{1}} = {2:{3}}".format(str(g), k1,
            power, k2))

def CheckIfSubgroupIsNormal(G, H):
    for h in H:
        for g in G:
            if not(g * h * G.Inv(g) in H):
                return False
    return True
'''
# Check if N=<(1, 1)> is a normal subgroup
c = ZQ(Z(1), Q(0, 1))
N = Group([c ** 0, c ** 1, c ** 2])
print("N = {0}".format(N))
print("The <{0}> group is normal: {1}".
        format(c, CheckIfSubgroupIsNormal(G, N)))

# Check if N=<(2, 1)> is a normal subgroup
c = ZQ(Z(2), Q(0, 1))
N = Group([c ** 0, c ** 1, c ** 2])
print("N = {0}".format(N))
print("The <{0}> group is normal: {1}".
        format(c, CheckIfSubgroupIsNormal(G, N)))

# Check if N=<(0, i)> is a normal subgroup
c = ZQ(Z(0), Q(2, 1))
N1 = Group([c ** 0, c ** 1, c ** 2, c ** 3])
print("N1 = {0}".format(N1))
print("The <{0}> group is normal: {1}".
        format(c, CheckIfSubgroupIsNormal(G, N)))

# Find the Left classes smezhnosty
for g in G.members:
    print("gH, where g = {0}:".format(g))
    print("\t" + str(ClassSmezh(g, N)))

# Cayley table of the G/N factor-group
def CayleyTableFactor(G, H):
    GH = FactorGroup(G, H)
    k = 7
    print(' ' * k, end=' ‖ ')
    for c in GH.members:
        print("{0:{1}}".format(str(c.Member()), k), end=' | ')
    print('\n' + '=' * ((k + 3) * (len(GH.members) + 1)))
    for c1 in GH.members:
        print("{0:{1}}".format(str(c1.Member()), k), end=' ‖ ')
        for c2 in GH.members:
            print("{0:{1}}".format(str((c1 * c2).Member()),
                k), end=' | ')
        print()
CayleyTableFactor(G, N)

# Cayley table of the Q8 group
def CayleyTable(G):
    k = 2
    print(' ' * k, end=' ‖ ')
    for c in G.members:
        print("{0:{1}}".format(str(c), k), end=' | ')
    print('\n' + '=' * ((k + 3) * (len(G.members) + 1)))
    for c1 in G.members:
        print("{0:{1}}".format(str(c1), k), end=' ‖ ')
        for c2 in G.members:
            print("{0:{1}}".format(str(c1 * c2),
                k), end=' | ')
        print()
Quat = Group([Q(q, s) for q in range(4)
    for s in range(1, -2, -2)])
CayleyTable(Quat)

# All the Commutators of G
comm = Commutant()
for g1 in G.members:
    for g2 in G.members:
        c = Commutator(g1, g2)
        if not(c in comm.members):
            comm.Add(c)
print(comm)
'''
