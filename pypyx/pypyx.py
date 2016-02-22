#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import pyx
### supports LaTeX!
import pyx.metapost.path

import math as maths

class pypyx_maths:

	@staticmethod
	def degrees (d):
		return (2 * maths.pi) * d / 360

	@staticmethod
	def gradient (g):
		if type(g).__name__ == 'tuple':
			(x, y) = g
			return maths.atan2(y, x)
		else:
			return maths.atan(g)

class colour:

	########################
	### COLOUR SELECTION

	@staticmethod
	def rgb ((r, g, b)):
		return pyx.color.rgb (r, g, b)

	### chroma is 'circular':
	### 0.0 = red
	### 1.0 = yellow
	### 2.0 = green
	### 3.0 = cyan
	### 4.0 = blue
	### 5.0 = magenta
	### 6.0 = back to red
	@staticmethod
	def hue (chroma):
		chroma = chroma % 6
		if chroma < 0:
			chroma += 6
		return pyx.color.hsb (chroma / 6, 1, 1)

	@staticmethod
	def grey (value = 0.5):
		return pyx.color.gray (value)

	########################
	### NAMED COLOURS

	@staticmethod
	def black ():
		return pyx.color.rgb.black

	@staticmethod
	def dark_grey ():
		return pyx.color.gray (1/4)

	@staticmethod
	def mid_grey ():
		return pyx.color.gray (1/2)

	@staticmethod
	def light_grey ():
		return pyx.color.gray (3/4)

	@staticmethod
	def white ():
		return pyx.color.rgb.white

	@staticmethod
	def red ():
		return pyx.color.rgb.red

	@staticmethod
	def pink ():
		return pyx.color.rgb (1, 1/2, 1/2)

	@staticmethod
	def orange ():
		return pyx.color.rgb (1, 1/2, 0)

	@staticmethod
	def brown ():
		return pyx.color.rgb (1/2, 1/4, 0)

	@staticmethod
	def yellow ():
		return pyx.color.rgb (1, 1, 0)

	@staticmethod
	def lime ():
		return pyx.color.rgb (2/3, 1, 0)

	@staticmethod
	def green ():
		return pyx.color.rgb.green

	### (turquoise)
	@staticmethod
	def cyan ():
		return pyx.color.rgb (0, 1, 1)

	@staticmethod
	def blue ():
		return pyx.color.rgb.blue

	@staticmethod
	def magenta ():
		return pyx.color.rgb (1, 0, 1)

	@staticmethod
	def purple ():
		return pyx.color.rgb (1/2, 0, 1/2)

class pic:

	class mode:

		def __init__ (self, scale):
			self.scale = scale
			self.common_styles = [
				]
			self.colour = colour.black()
			self.stroke_styles = [
					pyx.style.linecap.round,
				]
			self.text_halign = pyx.text.halign.center
			self.text_valign = pyx.text.valign.middle
			self.text_styles = [
				]

	class ctx:

		def __init__ (self, c, m):
			self.c = c
			self.m = m

		########################
		### LINE STYLES

		def dotted (self):
			self.m.stroke_styles.append (
					pyx.style.linestyle.dotted
				)
			return self

		def dashed (self):
			self.m.stroke_styles.append (
					pyx.style.linestyle.dashed
				)
			return self

		def unstroked (self):
			self.m.colour = None;
			return self

		def colour (self, col):
			self.m.colour = col;
			return self

		def filled (self, col):
			self.m.stroke_styles.append (
					pyx.deco.filled ([col])
				)
			return self

		def transparent (self, value):
			self.m.common_styles.append (
					pyx.color.transparency (value)
				)
			return self

		def opaque (self, value):
			return self.transparent (1 - value)

		def to_left (self):
			self.m.text_halign = pyx.text.halign.right
			return self

		def centre (self):
			self.m.text_halign = pyx.text.halign.center
			return self

		def to_right (self):
			self.m.text_halign = pyx.text.halign.left
			return self

		def above (self):
			self.m.text_valign = pyx.text.valign.bottom
			return self

		def middle (self):
			self.m.text_valign = pyx.text.valign.middle
			return self

		def below (self):
			self.m.text_valign = pyx.text.valign.top
			return self


		########################
		### PAINT OPERATIONS

		def text (self, (x, y), t):
			c = self.c
			m = self.m
			s = m.scale

			c.text (
					x * s, y * s,
					t,
					m.common_styles +
					[
						m.colour,
						m.text_halign,
						m.text_valign,
					] +
					m.text_styles
				)
			return self

		def __stroke_styles (self):
			m = self.m
			styles = \
					m.common_styles + \
					m.stroke_styles
			if m.colour != None:
				#styles.append (pyx.deco.stroked([m.colour]))
				styles.append (pyx.deco.stroked)
				styles.append (m.colour)
			return styles

		def point (self, p):
			return self.line (p, p)

		def line (self, (x1, y1), (x2, y2)):
			c = self.c
			m = self.m
			s = m.scale

			c.draw (pyx.path.line (
						x1 * s, y1 * s,
						x2 * s, y2 * s
					),
					self.__stroke_styles()
				)
			return self

		def __open_smooth_poly_curve (self, xys, start_angle = None, finish_angle = None):
			c = self.c
			m = self.m
			s = m.scale

			pathitems=[]

			if len(xys) >= 2:
				xy = xys[0]
				(x, y) = xy
				if start_angle == None:
					startknot = pyx.metapost.path.beginknot (s * x, s * y)
				else:
					angle = 360 * start_angle / (2 * maths.pi)
					startknot = pyx.metapost.path.beginknot (s * x, s * y, curl = None, angle = angle)
				pathitems.append (startknot)

			pathitems.append (pyx.metapost.path.curve())

			for idx in xrange (1, len(xys) - 1):

				xy = xys[idx]
				(x, y) = xy
				knot = pyx.metapost.path.knot (s * x, s * y)
				pathitems.append (knot)

				pathitems.append (pyx.metapost.path.curve())

			if len(xys) >= 2:
				xy = xys[-1]
				(x, y) = xy
				if finish_angle == None:
					finishknot = pyx.metapost.path.endknot (s * x, s * y)
				else:
					angle = 360 * finish_angle / (2 * maths.pi)
					finishknot = pyx.metapost.path.endknot (s * x, s * y, curl = None, angle = angle)
				pathitems.append (finishknot)

			c.draw (pyx.metapost.path.path (
						pathitems
					),
					self.__stroke_styles()
				)
			return self

		def smooth_poly_curve (self, xys, start_angle = None, finish_angle = None):
			self.__open_smooth_poly_curve (xys, start_angle = start_angle, finish_angle = finish_angle)
			return self

		def circle (self, (x, y), r):
			c = self.c
			m = self.m
			s = m.scale
			c.draw (pyx.path.circle (
						x * s, y * s,
						r * s
					),
					self.__stroke_styles()
				)
			return self

		########################

	def __init__ (self, scale = 1.0):

		self.scale = scale
		self.c = pyx.canvas.canvas()

	def op (self):

		return self.ctx (self.c, self.mode (scale = self.scale))

	def output_pdf (self, name):
		self.c.writePDFfile (name)

		#c.writeEPSfile()
		### c.writeSVGfile() not in this version of PyX

if __name__ == '__main__':
	pass
