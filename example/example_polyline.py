#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
from pypyx.pypyx import colour, pic

p = pic (scale = 1)

num_pts = 5
step = 2
r = 0.5

tau = 2 * maths.pi
pts = []

for idx in xrange(0, num_pts):
	a = tau * idx * step / num_pts
	x = r * maths.sin(a)
	y = r * maths.cos(a)

	pts.append ((x, y))

p.op().parity_winding().filled(colour.grey(0.5)).closed().poly_line (
		pts
	)

p.output_pdf('pentagram')
