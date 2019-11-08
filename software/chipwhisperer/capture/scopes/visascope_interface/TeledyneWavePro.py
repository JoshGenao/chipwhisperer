from ._base import VisaScope
from chipwhisperer.common.utils import util


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
 
    
    def default_setup(self):
        """
        Sets up capture default for this scope

        *   45dB gain
        *
        *
        """
        self.gain.db = 45

    def con(self):
        pass
    
    def dis(self):
        pass

    def arm(self):
        pass

    def capture(self):
        pass

    def get_name(self):
        return self._name


    getName = util.camel_case_deprecated(get_name)