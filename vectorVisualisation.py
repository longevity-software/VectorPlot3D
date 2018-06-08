import math
import sys

from PyQt5 import QtWidgets

import Gui
    
# main entry point
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Gui.Gui()
    sys.exit(app.exec_())
