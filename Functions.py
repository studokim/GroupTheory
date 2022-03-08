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

def GenerateGroup(g, additive = False):
    lis = []
    res = g
    if (additive):
        while not(res in lis):
            lis.append(res)
            res += g
    else:
        while not(res in lis):
            lis.append(res)
            res *= g
    return Models.Group(lis, additive)

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

def CheckIfSubgroupIsNormal(G, H, printable = False):
    k = len(str(G.Neutral())) + 1
    for ig in range(G.Ord()):
        g = G[ig]
        for ih in range(H.Ord()):
            h = H[ih]
            res = g * h * G.Inv(g)
            if (printable):
                print("{0:{4}} * {1:{4}} * {2:{4}} = {3:{4}}"
                    .format(str(g), str(h),
                        str(G.Inv(g)), str(res), k))
            if not(res in H):
                return False
    return True

def PrintIfSubgroupIsNormal(G, H, printable = False):
    print("The given subgroup is normal: {0}".
        format(CheckIfSubgroupIsNormal(G, H, printable)))

def PrintIfGeneratedSubgroupIsNormal(G, c, printable = False):
    H = GenerateGroup(c)
    print("The <{0}> subgroup is normal: {1}".
        format(c, CheckIfSubgroupIsNormal(G, H, printable)))

# Find the Left or Right classes smezhnosty
def PrintClasses(G, H, left = True):
    lis = []
    for g in G:
        c = Models.ClassSmezh(g, H, left)
        if not(c in lis):
            lis.append(c)
            title = "gH" if left else "Hg"
            print(title + ", where g = {0}:\t{1}".format(g, c))

def CayleyTable(G):
    k = len(str(G.Neutral())) + 1
    print(' ' * k, end=' ‖ ')
    for ig in range(G.Ord()):
        g = G[ig]
        print("{0:{1}}".format(str(g), k), end=' | ')
    print('\n' + '=' * ((k + 3) * (G.Ord() + 1)))
    for ig1 in range(G.Ord()):
        g1 = G[ig1]
        print("{0:{1}}".format(str(g1), k), end=' ‖ ')
        for ig2 in range(G.Ord()):
            g2 = G[ig2]
            print("{0:{1}}".format(str(g1 * g2), k), end=' | ')
        print()

def GetOrders(G):
    e = G.Neutral()
    res = []
    for i in range(G.Ord()):
        g = G[i]
        power = 1
        while not (g ** power == e):
            power += 1
        res.append(power)
    return res

def PrintSubgroupWithOrder(G, order):
    orders = GetOrders(G)
    subgroups = []
    for i in range(G.Ord()):
        if (orders[i] == order):
            H = GenerateGroup(G[i])
            if not(H in subgroups):
                subgroups.append(H)
    if (len(subgroups) == 0):
        print("There's no H < G: |H| = {0}".format(order))
    else:
        for H in subgroups:
            print(H)
