

import numpy
import random
from mayavi import mlab

niveles = 11
tam = 2 ** (niveles - 1)
altura  = numpy.zeros((tam + 1, tam + 1))

for elev in range(niveles):
  paso = tam // 2 ** elev
  for y in range(0, tam + 1, paso):

    salto = 1 - (y // paso) % 2 if elev > 0 else 0

    for x in range(paso * salto, tam + 1, paso * (1 + salto)):

      pointer = 1 - (x // paso) % 2 + 2 * salto if elev > 0 else 3
      yref, xref = paso * (1 - pointer // 2), paso * (1 - pointer % 2)
      esq1 = altura[y - yref, x - xref]
      esq2 = altura[y + yref, x + xref]
      prom = (esq1 + esq2) / 2.0
      var = paso * (random.random() - 0.5)
      altura[y,x] = prom + var if elev > 0 else 0

xg, yg = numpy.mgrid[-10:1:10j * tam, -10:1:10j * tam]
surf = mlab.surf(xg, yg, altura, colormap='gist_earth', warp_scale='auto')

mlab.show()

