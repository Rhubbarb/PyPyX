#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
import os
from pypyx.pypyx import pic, pypyx_maths

p = pic (scale = 0.25)

o_x = 10
o_y = 10
o = (o_x, o_y)

n = 20

for i in xrange (0, n+1):

	a = pypyx_maths.tau * i / n;
	a2 = a/2

	#print i, a2, a

	sx = o_x + (i + 2) * maths.cos(a2)
	sy = o_y + (i + 2) * maths.sin(a2)

	p.op().arc (o, (sx,sy), a)

p.output_pdf (os.path.splitext(__file__)[0])
