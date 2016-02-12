# PyPyX
A friendlier Pythonic interface to PyX

[PyX](http://pyx.sourceforge.net/) is a wonderful library for drawing (mathematical) diagrams in Python; it has support for [LaTeX](https://en.wikipedia.org/wiki/LaTeX).

This is intended as a simpler interface to PyX, for simple line drawings.

Example:

```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import math as maths
from pypyx.pypyx import colour, pic

p = pic (scale = 4.0)

r2 = maths.sqrt(2)

o = (0, 0)
x = (r2, 0)
y = (0, 1)
xy = (r2, 1)

p.op().colour(colour.light_grey()).circle ((r2/2, 1/2), maths.sqrt(3) / 2)

p.op().dotted().line (o, x)
p.op().line (o, y)
p.op().dashed().colour(colour.red()).line (y, xy)
p.op().line (x, xy)

p.op().text ((r2/2, 1/2), 'A4')

p.output_pdf ('Silly_A4_Paper_Example')
```

![Silly_A4_Paper_Example](/example/Silly_A4_Paper_Example.png)
