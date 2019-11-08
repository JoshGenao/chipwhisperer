#!/usr/bin/python
# HIGHLEVEL_CLASSLOAD_FAIL_FUNC_DEBUG

# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
# All rights reserved.
#
# Authors: Colin O'Flynn
#
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================

from .base import ScopeTemplate
from chipwhisperer.common.utils import util
from .visascope_interface.TeledyneWavePro import VisaScopeInterface_TeledyneWavePro
import visa

class VisaScope(ScopeTemplate, util.DisableNewAttr):
    _name = "VISA Scope"

    def __init__(self):
        ScopeTemplate.__init__(self)
        self._is_connected = False
        # Default: Scope Type = Teledyne Wave Pro 604 HD
        self.scopetype = VisaScopeInterface_TeledyneWavePro()

    def setCurrentScope(self, scope):
        self.scopetype = scope
        if scope is not None:
            self.scopetype.dataUpdated.connect(self.newDataReceived)

    def _con(self):
        if self.scopetype is not None:
            self.scopetype.con()
            return True
        return False

    def _dis(self):
        if self.scopetype is not None:
            self.scopetype.dis()

    def arm(self):
        try:
            self.scopetype.arm()
        except Exception:
            self.dis()
            raise

    def capture(self):
        """Raises IOError if unknown failure, returns 'False' if successful, 'True' if timeout"""
        return self.scopetype.capture()