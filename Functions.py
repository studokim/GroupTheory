import Models
import CurrentGroup

# Fill the G=Z/3Z*Q8 group
def MakeMyGroup():
    lis = []
    for z in range(3):
        for q in range(4):
            for s in range(1, -2, -2):
                lis.append(CurrentGroup.ZQ(z, q, s))
    print(lisgi)
    return Models.Group(lis)

'''
# Calculate orders of the G=Z/3Z*Q8 group members
for g in G.members:
    power = 1
    while not (g ** power == e):
        power += 1
    print("ord {0:7} = {1:2}".format(g, power))

# Fill the inverses (the same G group actually)
G_inv = Group([])
for g in G.members:
    for h in G.members:
        if (g*h == e):
            G_inv.Add(h)
print("G_inv = {0}".format(G_inv))

def CheckIfSubgroupIsNormal(G, H):
   for h in H.members:
       for i in range(len(G.members)):
            if not(G.members[i] * h * G_inv.members[i]
                    in N.members):
                return False
    return True

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
