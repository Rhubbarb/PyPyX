#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
from pypyx.pypyx import colour, pic

def deg (d):
	return (2 * maths.pi) * d / 360

p = pic (scale = 2)

tau = 2 * maths.pi

p.op().dashed().smooth_poly_curve (
		[
			(0, 0),
			(tau/4, 1),
			(tau/2, 0),
			(3*tau/4, -1),
			(tau, 0),
		]
	)

p.op().closed().smooth_poly_curve (
		[
			(0, 0),
			(tau/4, 1),
			(tau/2, 0),
			(3*tau/4, -1),
			(tau, 0),
		]
	)

p.output_pdf('loop')
