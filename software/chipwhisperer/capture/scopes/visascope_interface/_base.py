import logging
import time
import visa
from chipwhisperer.common.utils import util


class VisaScope(object):
    _name = 'Scope Settings'

    def __init__(self):
        self.visaInst = None

    def con(self):
        pass

    def dis(self):
        pass

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
