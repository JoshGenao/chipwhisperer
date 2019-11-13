#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
#    This file is an addition to the chipwhisperer software baseline. This
#    file allows the interface of a VISA connected oscilloscope (in this
#    case the Teledyne WavePro 604)
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
from ._base import VisaScope
from chipwhisperer.common.utils import util
import logging


class VisaScopeInterface_TeledyneWavePro(VisaScope, util.DisableNewAttr):
    """ Teledyne WavePro 604 object.

    This class contains the public API for the Teledyne WavePro hardware. It 
    includes specific setting for each of these devices.

    To connect to one of these devices, the easiest method is::

            import chipwhisperer as cw
            scope = cw.scope(type=scopes.TeledyneWavePro)

    For more help about scope settings, try help() on each of the ChipWhisperer
    scope submodules (scope.adc, scope.io, scope.glitch):

        *  :attr:`scope.gain <.TeledyneWavePro.gain>`
        *  :attr:`scope.adc <.TeledyneWavePro.adc>`
        *  :attr:`scope.clock <.TeledyneWavePro.clock>`
        *  :attr:`scope.io <.TeledyneWavePro.io>`
        *  :attr:`scope.trigger <.TeledyneWavePro.trigger>`
        *  :meth:`scope.default_setup <.TeledyneWavePro.default_setup>`
        *  :meth:`scope.con <.TeledyneWavePro.con>`
        *  :meth:`scope.dis <.TeledyneWavePro.dis>`
        *  :meth:`scope.arm <.TeledyneWavePro.arm>`
        *  :meth:`scope.get_last_trace <.TeledyneWavePro.get_last_trace>`
    """
    _name = "Teledyne WavePro604 HD"

    # Constructor
    def __init__(self):
        self._lasttrace = None
        VisaScope.__init__()

    def con(self):
        logging.info(self.visaInst.query('*IDN?'))
        logging.info('Setting to default settings')
        # Don't return the command header with query results
        self.visaInst.write(self.header)
        # Recall default setup
        self.visaInst.write(r"""vbs 'app.settodefaultsetup' """)
        # Wait until scope is done with recall default
        self.visaInst.write(r"""vbs? 'return=app.WaitUntilIdle(5)' """)

    def arm(self):
        # Set up acquisition trigger and timebase
        self.visaInst.write(r"""vbs 'app.acquisition.triggermode = "stopped" ' """)
        self.visaInst.write(r"""vbs 'app.acquisition.trigger.edge.level = 1.0' """)
        self.visaInst.write(r"""vbs 'app.acquisition.triggermode = "single" ' """)
        self.visaInst.write(r"""vbs 'app.acquisition.horizontal.maximize = "FixedSampleRate" ' """)
        # Clear all current measurement definitions and set up new measurement 
        self.visaInst.write(r"""vbs 'app.measure.clearall ' """)
        self.visaInst.write(r"""vbs 'app.measure.showmeasure = true ' """)
        self.visaInst.write(r"""vbs 'app.measure.statson = true ' """)
        self.visaInst.write(r"""vbs 'app.measure.p1.view = true ' """)
        self.visaInst.write(r"""vbs 'app.measure.p1.paramengine = "mean" ' """)
        self.visaInst.write(r"""vbs 'app.measure.p1.source1 = "C1" ' """)
        # Reset the parameter statistics
        self.visaInst.write(r"""vbs 'app.measure.clearsweeps ' """)

    def capture(self):
        """ Raises IOError if unknown failure, return 'True' if timeout, 'False' if no timeout """

        # Use a 0.1 sec timeout in case the acquisition is not complete
        r = self.visaInst.query(r"""vbs? 'return=app.aquisition.acquire( 0.1, True )' """)

        if r == 0:
            logging.warning('Timeout in Teledyne WavePro capture()')
            return True
        
        self._lasttrace = self.visaInst.query(r"""vbs? 'return=app.measure.p1.out.result.value' """)
        return False

    def get_last_trace(self):
        """ Returns the last trace captured with this scope """
        return self._lasttrace

    getLastTrace = util.camel_case_deprecated(get_last_trace)