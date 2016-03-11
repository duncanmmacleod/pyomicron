# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2016)
#
# This file is part of PyOmicron.
#
# PyOmicron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyOmicron is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyOmicron.  If not, see <http://www.gnu.org/licenses/>.

"""Test parameter handling for Omicron
"""

import os
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from omicron import utils


class UtilsTestCase(unittest.TestCase):
    def test_get_omicron_version(self):
        testv = 'v2r1'
        v = utils.get_omicron_version(
            "/home/detchar/opt/virgosoft/Omicron/%s/Linux-x86_64/omicron.exe"
            % testv
        )
        self.assertEqual(v, testv)
        os.environ['OMICRON_VERSION'] = testv
        self.assertEqual(utils.get_omicron_version(), testv)
        os.environ.pop('OMICRON_VERSION')
        os.environ['OMICRONROOT'] = (
            "/home/detchar/opt/virgosoft/Omicron/%s" % testv)
        self.assertEqual(utils.get_omicron_version(), testv)
        self.assertGreater(utils.get_omicron_version(), 'v1r2')
        self.assertLess(utils.get_omicron_version(), 'v2r2')