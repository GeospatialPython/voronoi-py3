#! /usr/bin/env python

from distutils.core import setup

DESCRIPTION = """\
Python 3 port of voronoi.py.

Voronoi diagram calculator/ Delaunay triangulator
Translated to Python by Bill Simons
September, 2005

Ported to Python 3 by Joel Lawhead (GeospatialPython.com)
August 2015

Calculate Delaunay triangulation or the Voronoi polygons for a set of 
2D input points.

Derived from code bearing the following notice:

The author of this software is Steven Fortune.  Copyright (c) 1994 by AT&T
Bell Laboratories.
Permission to use, copy, modify, and distribute this software for any
purpose without fee is hereby granted, provided that this entire notice
is included in all copies of any software which is or includes a copy
or modification of this software and in all copies of the supporting
documentation for such software.
THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
WARRANTY.  IN PARTICULAR, NEITHER THE AUTHORS NOR AT&T MAKE ANY
REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.

Comments were incorporated from Shane O'Sullivan's translation of the 
original code into C++ (http://mapviewer.skynet.ie/voronoi.html)

Steve Fortune's homepage: http://netlib.bell-labs.com/cm/cs/who/sjf/index.html
"""

def run():
    setup(name="voronoi",
        version="1.0",
        description="Calculate Delaunay triangulation or the Voronoi polygons for a set of 2D input points",
        url="https://github.com/GeospatialPython/voronoi-py3/",
        license="MIT",
        author="Steve Fortune",
        maintainer_email="jlawhead@geospatialpython.com",
        packages=["voronoi"],
        long_description=DESCRIPTION,
        download_url=
            "https://github.com/GeospatialPython/voronoi-py3/archive/master.zip",
        platforms=["OS Independent"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: MIT",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Scientific/Engineering :: GIS",
            "Topic :: Database",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )

if __name__ == "__main__":
    run()

# vim: set et sts=4 sw=4 :
