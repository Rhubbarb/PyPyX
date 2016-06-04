#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
import os
from pypyx.pypyx import colour, pic

p = pic (scale = .15)

x = 0

def pos ():
	global x
	x += 1
	return (0, x)

p.op().stroked(colour.red()).text (pos(), 'red')
p.op().stroked(colour.orange()).text (pos(), 'orange')
p.op().stroked(colour.yellow()).text (pos(), 'yellow')
p.op().stroked(colour.lime()).text (pos(),'lime')
p.op().stroked(colour.green()).text (pos(), 'green')
p.op().stroked(colour.cyan()).text (pos(), 'cyan')
p.op().stroked(colour.blue()).text (pos(), 'blue')
p.op().stroked(colour.magenta()).text (pos(), 'magenta')
p.op().stroked(colour.white()).text (pos(), 'white')
p.op().stroked(colour.black()).text (pos(), 'black')

p.op().stroked(colour.purple()).text (pos(), 'purple')
p.op().stroked(colour.brown()).text (pos(), 'brown')
p.op().stroked(colour.pink()).text (pos(), 'pink')

p.op().stroked(colour.dark_grey()).text (pos(), 'dark grey')
p.op().stroked(colour.grey()).text (pos(), 'grey')
p.op().stroked(colour.mid_grey()).text (pos(), 'mid-grey')
p.op().stroked(colour.light_grey()).text (pos(), 'light grey')
p.op().stroked(colour.black()).text (pos(), 'black')
p.op().stroked(colour.rgb((.9,.7,.5))).text (pos(), 'rgb')

#for i in xrange (-24, 25):
#for i in xrange (0, 25):
#	h = i / 4
#	text = 'hue=' + str(h)
#	p.op().stroked(colour.hue(h)).text (pos(), text)

#for i in xrange (0, 11):
#	v = i / 10
#	text = 'grey=' + str(v)
#	p.op().stroked(colour.grey(v)).text (pos(), text)

p.output_pdf (os.path.splitext(__file__)[0])
