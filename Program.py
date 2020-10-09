#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Models
import MyGroup
import Functions

G = Functions.MakeMyGroup()
e = G.Neutral()

#print("G = {0}".format(G))
#print("e = {0}".format(e))
#Functions.PrintOrders(G)

# Check if N=<(1, 1)> is a normal subgroup
c = MyGroup.ZQ(1, 0, 1)
N = Models.Group([c ** 0, c ** 1, c ** 2])
print("N = {0}".format(N))
print("The <{0}> group is normal: {1}".
        format(c, Functions.CheckIfSubgroupIsNormal(G, N)))
