#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Models
import MyGroup
import Functions

def PrintTask(n):
    k = 29
    print('\n')
    print('#' * k + " TASK {0} ".format(n) + '#' * k)
    print()

G = Functions.MakeMyGroup()
#print("G = {0}".format(G))

'''task 1'''
PrintTask(1)
Functions.PrintOrders(G)

'''task 2'''
PrintTask(2)
H = Functions.GenerateGroup(MyGroup.ZQ(0, 3, 1))
print("H = <0, k> = {0}".format(str(H)))
Functions.PrintIfSubgroupIsNormal(G, H)
Functions.PrintClasses(G, H)
print('*' * 58)
Functions.PrintClasses(G, H, left=False)

'''task 3'''
PrintTask(3)
H = Functions.GenerateGroup(MyGroup.ZQ(1, 0, 1))
print("H = <1, 1> = {0}".format(str(H)))
Functions.PrintIfSubgroupIsNormal(G, H)
print("Cayley table of the G/H FactorGroup:")
GH = Models.FactorGroup(G, H)
Functions.CayleyTable(GH)

'''task 4'''
PrintTask(4)
print("Cayley table of the Group of Quaternions:")
Quat = Models.Group([MyGroup.Q(q, s) for q in range(4)
    for s in range(1, -2, -2)])
Functions.CayleyTable(Quat)

'''task 5'''
PrintTask(5)
print("Commutant of the G group:")
print(Models.Commutant(G))
