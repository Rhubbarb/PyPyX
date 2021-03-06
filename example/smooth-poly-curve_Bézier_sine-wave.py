#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
import os
from pypyx.pypyx import colour, pic

def deg (d):
	return (2 * maths.pi) * d / 360

p = pic (scale = 2)

tau = 2 * maths.pi
bit = 0.1
tick = 0.05

### label
p.op().text ((tau/2, 1), 'sine')

### axes
p.op().line ((-bit, 0), (tau+bit, 0))
p.op().line ((0, -(1+bit)), (0, 1+bit))

### axis ticks and labels
p.op().to_left().below().text ((-tick, -tick), r'$0$')
p.op().line ((tau/4, -tick), (tau/4, 0))
p.op().below().text ((tau/4, -tick), r'$\tau/4$')
p.op().line ((tau/2, -tick), (tau/2, 0))
p.op().to_left().below().text ((tau/2, -tick), r'$\tau/2$')
p.op().line ((3*tau/4, -tick), (3*tau/4, 0))
p.op().below().text ((3*tau/4, -tick), r'$3\tau/4$')
p.op().line ((tau, -tick), (tau, 0))
p.op().below().text ((tau, -tick*2), r'$\tau$')
p.op().line ((-tick, 1), (0, 1))
p.op().to_left().text ((-tick, 1), r'$1$')
p.op().line ((-tick, -1), (0, -1))
p.op().to_left().text ((-tick, -1), r'$-1$')

p.op().stroked(colour.green()).smooth_poly_curve (
		[
			(0, 0),
			(tau/4, 1),
		],
		start_angle = deg(45),
		finish_angle = deg(0)
	)

p.op().stroked(colour.green()).smooth_poly_curve (
		[
			(tau/4, 1),
			(tau/2, 0),
		],
		start_angle = deg(0),
		finish_angle = deg(-45)
	)

p.op().stroked(colour.red()).smooth_poly_curve (
		[
			(tau/2, 0),
			(3*tau/4, -1),
			(tau, 0),
		],
		start_angle = deg(-45),
		finish_angle = deg(45)
	)

#p.op().dashed().stroked(colour.pink()).curve (
#		[
#			(0, 0),
#			(tau/4, 1),
#			(tau/2, 0),
#			#(3*tau/4, -1),
#			#(tau, 0),
#		],
#		start_angle = deg(45),
#		finish_angle = deg(-45)
#	)

p.output_pdf (os.path.splitext(__file__)[0])
