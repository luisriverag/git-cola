# -*- coding: utf-8 -*-
#
# Copyright © 2014-2015 Colin Duquesnoy
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtDesigner classes and functions.
"""

from qtpy import PYQT5
from qtpy import PYQT4
from qtpy import PythonQtError


if PYQT5:
    from PyQt5.QtDesigner import *
elif PYQT4:
    from PyQt4.QtDesigner import *
else:
    raise PythonQtError('No Qt bindings could be found')
