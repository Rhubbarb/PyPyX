#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math

from pypyx.pypyx import pic

p = pic (scale = 4.0)

r2 = math.sqrt(2)

o = (0, 0)
x = (r2, 0)
y = (0, 1)
xy = (r2, 1)

p.op().light_grey().circle ((r2/2, 1/2), math.sqrt(3) / 2)

p.op().dotted().line (o, x)
p.op().line (o, y)
p.op().dashed().red().line (y, xy)
p.op().line (x, xy)

p.op().text ((r2/2, 1/2), 'A4')

p.output_pdf ('Silly_A4_Paper_Example')