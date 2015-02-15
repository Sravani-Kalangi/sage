# -*- encoding: utf-8 -*-
r"""
Catalog of all available output container types.

If you define another output type then you must add it to the imports here.
"""

#*****************************************************************************
#       Copyright (C) 2015 Volker Braun <vbraun.name@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#  as published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from .output_basic import (
    OutputPlainText,
    OutputAsciiArt,
    OutputMathJax,
)

from .output_graphics import (
    OutputImagePng,
    OutputImageGif,
    OutputImageJpg,
    OutputImageSvg,
    OutputImagePdf,
    OutputImageDvi,
)

from .output_graphics3d import (
    OutputSceneJmol,
    OutputSceneLightwave,
    OutputSceneCanvas3d,
)
