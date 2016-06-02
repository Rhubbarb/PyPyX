#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import math as maths
from pypyx.pypyx import colour, pic

p = pic (scale = .15)

x = 0

def pos ():
	global x
	x += 1
	return (0, x)

p.op().colour(colour.red()).text (pos(), 'red')
p.op().colour(colour.orange()).text (pos(), 'orange')
p.op().colour(colour.yellow()).text (pos(), 'yellow')
p.op().colour(colour.lime()).text (pos(),'lime')
p.op().colour(colour.green()).text (pos(), 'green')
p.op().colour(colour.cyan()).text (pos(), 'cyan')
p.op().colour(colour.blue()).text (pos(), 'blue')
p.op().colour(colour.magenta()).text (pos(), 'magenta')
p.op().colour(colour.white()).text (pos(), 'white')
p.op().colour(colour.black()).text (pos(), 'black')

p.op().colour(colour.purple()).text (pos(), 'purple')
p.op().colour(colour.brown()).text (pos(), 'brown')
p.op().colour(colour.pink()).text (pos(), 'pink')

p.op().colour(colour.dark_grey()).text (pos(), 'dark grey')
p.op().colour(colour.grey()).text (pos(), 'grey')
p.op().colour(colour.mid_grey()).text (pos(), 'mid-grey')
p.op().colour(colour.light_grey()).text (pos(), 'light grey')
p.op().colour(colour.black()).text (pos(), 'black')
p.op().colour(colour.rgb((.9,.7,.5))).text (pos(), 'rgb')

#for i in xrange (-24, 25):
#for i in xrange (0, 25):
#	h = i / 4
#	text = 'hue=' + str(h)
#	p.op().colour(colour.hue(h)).text (pos(), text)

#for i in xrange (0, 11):
#	v = i / 10
#	text = 'grey=' + str(v)
#	p.op().colour(colour.grey(v)).text (pos(), text)

p.output_pdf('colours')
