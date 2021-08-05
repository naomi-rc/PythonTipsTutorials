# solutions to targeting python 2 and 3

#   1) using future imports : from __future__ import function (i.e. )
#   2) renaming modules by using import mapping: import x as y
#       try:
#           import python_3_module as module
#       except ImportError:
#           import python_2_module as module
#   3) avoid using obsolte modules (12 removed in python 3) : from future.builtins.disables import *
#   4) pip installing standard library backups : enum34 (enum), singledispatch, pathlib, etc.
