#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

#import math as maths
from pypyx.pypyx import pypyx_maths as pm

print pm.gradient(0)
print pm.gradient(1/2)
print pm.gradient(1)
print pm.gradient(2)

print pm.gradient((1,0))
print pm.gradient((1,1))
print pm.gradient((0,1))
