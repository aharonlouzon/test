import dtlpy as dl
import logging
from package import Printer

logger = logging.getLogger(name=__name__)


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class

    """
    def __init__(self):
        self.printer = Printer()

    def run(self):
        self.printer.print()
        print('This is 8th commit')
