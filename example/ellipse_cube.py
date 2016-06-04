#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
import os

from pypyx.pypyx import colour, pic, pypyx_maths

p = pic (scale = 4.0)

o = (0, 0)
d = maths.sqrt(3) / 2

### o'clock positions
d2 = (d, .5)
d4 = (d, -.5)
d6 = (0, -1)
d8 = (-d, -.5)
d10 = (-d, .5)
d12 = (0, 1)

p.op().stroked(colour.grey()).line ((-d/2, .25), (d/2, .75))
p.op().stroked(colour.grey()).line ((d/2, .25), (-d/2, .75))

mj = d / maths.sqrt(2)
mn = mj / maths.sqrt(3)

p.op().dashed().stroked("red").ellipse((d/2, -.25), mj, mn, pypyx_maths.degrees(60))
p.op().dashed().stroked("green").ellipse((0, .5), mj, mn, pypyx_maths.degrees(0))
p.op().dashed().stroked("blue").ellipse((-d/2, -.25), mj, mn, pypyx_maths.degrees(-60))

p.op().stroked("red").ellipse((d/2, -.25), mj/2, mn/2, pypyx_maths.degrees(60))
p.op().stroked("green").ellipse((0, .5), mj/2, mn/2, pypyx_maths.degrees(0))
p.op().stroked("blue").ellipse((-d/2, -.25), mj/2, mn/2, pypyx_maths.degrees(-60))

p.op().line (o, d2)
p.op().line (o, d10)
p.op().line (o, d6)

p.op().line (d2, d12)
p.op().line (d2, d4)
p.op().line (d6, d4)
p.op().line (d6, d8)
p.op().line (d10, d12)
p.op().line (d10, d8)

p.output_pdf (os.path.splitext(__file__)[0])
