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

	@staticmethod
	def hypot ((x, y)):
		#return maths.sqrt (x^2 + y^2)
		return maths.sqrt (x*x + y*y)

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
		return pyx.color.grey (value)

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

	########################

	@staticmethod
	def colour_from_string (name):
		col = None

		if name == 'black': col = colour.black()
		elif name == 'blue': col = colour.blue()
		elif name == 'brown': col = colour.brown()
		elif name == 'cyan': col = colour.cyan()
		elif name == 'green': col = colour.green()
		elif name == 'grey(dark)': col = colour.dark_grey()
		elif name == 'grey(light)': col = colour.light_grey()
		elif name == 'grey(mid)' or name == 'grey': col = colour.mid_grey()
		elif name == 'lime': col = colour.lime()
		elif name == 'magenta': col = colour.magenta()
		elif name == 'orange': col = colour.orange()
		elif name == 'pink': col = colour.pink()
		elif name == 'purple': col = colour.purple()
		elif name == 'red': col = colour.red()
		elif name == 'white': col = colour.white()
		elif name == 'yellow': col = colour.yellow()
		else:
			raise exceptions.BaseException ('Error: unknown colour name "' + name + '"')
		return col

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
			self.fill_rule = pyx.style.fillrule.nonzero_winding
			self.path_closed = False

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

		def stroked (self, col):
			if type(col).__name__ == 'str':
				self.m.colour = colour.colour_from_string (col)
			elif type(col).__name__ == 'instance':
				if col.__class__.__module__ == 'pyx.color':
					self.m.colour = col
				else:
					#print col.__class__
					#print col.__class__.__module__
					#print col.__class__.__name__
					raise exceptions.BaseException ('Error: unsupported class "' + col.__class__.__module__ + '"')
			else:
				raise exceptions.BaseException ('Error: unsupported type "' + type(col).__name__ + '"')
			return self

		def filled (self, col):
			self.m.stroke_styles.append (
					pyx.deco.filled ([col])
				)
			return self

		def nonzero_winding (self):
			self.m.fill_rule = pyx.style.fillrule.nonzero_winding
			return self

		def parity_winding (self):
			self.m.fill_rule = pyx.style.fillrule.even_odd
			return self

		def closed (self):
			self.m.path_closed = True
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

		def styled (self, desc):

			words = desc.lower().split(' ')
			for word in words:
				if word == '': pass
				elif word == 'black': self.stroked(colour.black())
				elif word == 'blue': self.stroked(colour.blue())
				elif word == 'brown': self.stroked(colour.brown())
				elif word == 'cyan': self.stroked(colour.cyan())
				elif word == 'dashed': self.dashed()
				elif word == 'dotted': self.dotted()
				elif word == 'green': self.stroked(colour.green())
				elif word == 'grey(dark)': self.stroked(colour.dark_grey())
				elif word == 'grey(light)': self.stroked(colour.light_grey())
				elif word == 'grey(mid)' or word == 'grey': self.stroked(colour.mid_grey())
				elif word == 'lime': self.stroked(colour.lime())
				elif word == 'magenta': self.stroked(colour.magenta())
				elif word == 'orange': self.stroked(colour.orange())
				elif word == 'pink': self.stroked(colour.pink())
				elif word == 'purple': self.stroked(colour.purple())
				elif word == 'red': self.stroked(colour.red())
				elif word == 'white': self.stroked(colour.white())
				elif word == 'yellow': self.stroked(colour.yellow())
				else:
					raise exceptions.BaseException ('Error: unknown word "' + word + '"')

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
			styles.append (m.fill_rule)
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

		def curve (self, (x1, y1), (cx2, cy2), (cx3, cy3), (x4, y4)):
			c = self.c
			m = self.m
			s = m.scale

			c.draw (pyx.metapost.path.path ([
						pyx.metapost.path.knot (
								s * x1, s * y1
							),
						pyx.metapost.path.controlcurve (
								(s * cx2, s * cy2),
								(s * cx3, s * cy3)
							),
						pyx.metapost.path.knot (
								s * x4, s * y4
							),
					]),
					self.__stroke_styles()
				)
			return self

		def poly_line (self, xys):
			c = self.c
			m = self.m
			s = m.scale

			p = pyx.path.path()

			(x, y) = xys[0]
			p.append (pyx.path.moveto (s * x, s * y))

			for idx in xrange (1, len(xys)):
				(x, y) = xys[idx]
				p.append (pyx.path.lineto (s * x, s * y))

			if m.path_closed:
				p.append (pyx.path.closepath())

			c.draw (p,
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
			#return self

		def __closed_smooth_poly_curve (self, xys):
			c = self.c
			m = self.m
			s = m.scale

			pathitems=[]

			for idx in xrange (0, len(xys)):

				xy = xys[idx]
				(x, y) = xy
				knot = pyx.metapost.path.knot (s * x, s * y)
				pathitems.append (knot)

				pathitems.append (pyx.metapost.path.curve())

			c.draw (pyx.metapost.path.path (
						pathitems
					),
					self.__stroke_styles()
				)
			#return self

		def smooth_poly_curve (self, xys, start_angle = None, finish_angle = None):
			m = self.m

			if m.path_closed:
				self.__closed_smooth_poly_curve (xys)
			else:
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
