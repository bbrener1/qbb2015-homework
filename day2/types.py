#!/usr/bin/env python

# Integer
i = 1000

#Float
f = .3

#String 
s = "whatever"

#Boolean 

truth = True

#Lists -- by convention contains only one type 
l = [1,2,3,4]

#Tuples

t = (1,"foo",5.0)

# Dictionary
d1 = {"key":1,"lock":2}
d2 = dict(key1="whatever")

for value in [i, f, s, truth, l, t, d1, d2]:
    print value, type (value)