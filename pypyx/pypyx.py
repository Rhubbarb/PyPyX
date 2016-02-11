#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division

import pyx
### supports LaTeX!

class pic:

	class mode:

		def __init__ (self, scale):
			self.scale = scale
			self.common_styles = [
				]
			self.stroke_styles = [
					pyx.style.linecap.round,
				]
			self.text_styles = [
					pyx.text.halign.center,
					pyx.text.valign.middle,
				]

	class ctx:

		def __init__ (self, c, m):
			self.c = c
			self.m = m

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

		def light_grey (self):
			self.m.common_styles.append (
					pyx.color.gray(2/3)
				)
			return self

		def red (self):
			self.m.common_styles.append (
					pyx.color.rgb.red
				)
			return self

		def text (self, (x, y), t):
			c = self.c
			m = self.m
			s = m.scale
			c.text (
					x * s, y * s,
					t,
					m.common_styles +
					m.text_styles
				)
			return self

		def line (self, (x1, y1), (x2, y2)):
			c = self.c
			m = self.m
			s = m.scale
			c.stroke (pyx.path.line (
						x1 * s, y1 * s,
						x2 * s, y2 * s
					),
					m.common_styles +
					m.stroke_styles
				)
			return self

		def circle (self, (x, y), r):
			c = self.c
			m = self.m
			s = m.scale
			c.stroke (pyx.path.circle (
						x * s, y * s,
						r * s
					),
					m.common_styles +
					m.stroke_styles
				)
			return self

	def __init__ (self, scale = 1.0):

		self.scale = scale
		self.c = pyx.canvas.canvas()

	def op (self):

		return self.ctx (self.c, self.mode(scale = self.scale))

	def output_pdf (self, name):
		self.c.writePDFfile(name)

		#c.writeEPSfile()
		### c.writeSVGfile() not in this version of PyX

if __name__ == '__main__':
	pass