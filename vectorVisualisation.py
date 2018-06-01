import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import math3d
from PyQt5 import QtWidgets, QtCore

# main Gui class deals with showing the gui and responding to user input
class Gui(QtWidgets.QMainWindow):

    # Gui class constructor
    def __init__(self):
    
        super().__init__()

        # set up the gui window
        self.setWindowTitle("Vector Visualisation App")
        self.resize(500,500)
        self.move(100,100)

        # add graph plot
        self.__graphPlot = graphicalPlot(self)
        self.__graphPlot.move(10,10)
    
        # show the gui window
        self.show()

# Graph class deals with showing the vector graph
class graphicalPlot(FigureCanvas):

    # graphicalPlot class constructor
    def __init__(self, parent=None, width=100, height=50, dpi=100):
        
        # create a figure and axis
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.__graphAxis = fig.add_subplot(111)

        # set up the figure canvas
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, 
                                    QtWidgets.QSizePolicy.Expanding, 
                                    QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    
    # public method to update the graph
    def updateGraph(self):
        self.__graphAxis.cla()

# main entry point
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())