#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
#    This file is an addition to the chipwhisperer software baseline. This 
#    file allows the interface of a VISA connected oscilloscope.
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
# =================================================

import logging
import visa


class VISAConnectionError(Exception):
    def __init__(self, msg):
        self.msg = msg


class VisaScope(object):
    _name = 'Scope Settings'
    header = "COMM_HEADER OFF"

    def __init__(self):
        self.rm = visa.ResourceManager('@py')                        # Will not be using VISA drivers
        resources = self.rm.list_resources()
        if resources:
            self.visaInst = self.rm.open_resource(resources[0])      # This needs to be fixed
        else:
            raise VISAConnectionError("No Resources Found")

    def con(self):
        logging.info(self.visaInst.query('*IDN?'))

    def dis(self):
        self.visaInst.close()
        self.rm.close()

    def updateCurrentSettiings(self):
        pass

    def currentSetting(self):
        """You must implement this"""
        pass

    def arm(self):
        """Example arm implementation works on most"""
        self.visaInst.write(":DIGitize")

    def capture(self):
        """ You MUST implement this"""
        pass
