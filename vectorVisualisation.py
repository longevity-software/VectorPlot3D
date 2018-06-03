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

        self.__initGui()

    def __initGui(self):

        # set up the gui window
        self.setWindowTitle("Vector Visualisation App")
        self.resize(490,700)
        self.move(100,0)

        # add vector input controls

        # vector 1
        vector1HeadingLabel = QtWidgets.QLabel("Vector 1", self)
        vector1HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1HeadingLabel.resize(490, 20)
        vector1HeadingLabel.move(0,0)

        vector1XLabel = QtWidgets.QLabel("X", self)
        vector1XLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1XLabel.resize(150,20)
        vector1XLabel.move(10,20)

        self.__vector1XInput = QtWidgets.QLineEdit(self)
        self.__vector1XInput.resize(150, 20)
        self.__vector1XInput.move(10,40)
        
        vector1YLabel = QtWidgets.QLabel("Y", self)
        vector1YLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1YLabel.resize(150,20)
        vector1YLabel.move(170,20)

        self.__vector1YInput = QtWidgets.QLineEdit(self)
        self.__vector1YInput.resize(150, 20)
        self.__vector1YInput.move(170,40)
        
        vector1ZLabel = QtWidgets.QLabel("Z", self)
        vector1ZLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1ZLabel.resize(150,20)
        vector1ZLabel.move(330,20)

        self.__vector1ZInput = QtWidgets.QLineEdit(self)
        self.__vector1ZInput.resize(150, 20)
        self.__vector1ZInput.move(330,40)

        # vector 2
        vector2HeadingLabel = QtWidgets.QLabel("Vector 2", self)
        vector2HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2HeadingLabel.resize(490, 20)
        vector2HeadingLabel.move(0,60)

        vector2XLabel = QtWidgets.QLabel("X", self)
        vector2XLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2XLabel.resize(150,20)
        vector2XLabel.move(10,80)

        self.__vector2XInput = QtWidgets.QLineEdit(self)
        self.__vector2XInput.resize(150, 20)
        self.__vector2XInput.move(10,100)
        
        vector2YLabel = QtWidgets.QLabel("Y", self)
        vector2YLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2YLabel.resize(150,20)
        vector2YLabel.move(170,80)

        self.__vector2YInput = QtWidgets.QLineEdit(self)
        self.__vector2YInput.resize(150, 20)
        self.__vector2YInput.move(170,100)
        
        vector2ZLabel = QtWidgets.QLabel("Z", self)
        vector2ZLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2ZLabel.resize(150,20)
        vector2ZLabel.move(330,80)

        self.__vector2ZInput = QtWidgets.QLineEdit(self)
        self.__vector2ZInput.resize(150, 20)
        self.__vector2ZInput.move(330,100)
        
        # vector 3 
        vector3HeadingLabel = QtWidgets.QLabel("Vector 3", self)
        vector3HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3HeadingLabel.resize(490, 20)
        vector3HeadingLabel.move(0,120)

        vector3XLabel = QtWidgets.QLabel("X", self)
        vector3XLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3XLabel.resize(150,20)
        vector3XLabel.move(10,140)

        self.__vector3XInput = QtWidgets.QLineEdit(self)
        self.__vector3XInput.resize(150, 20)
        self.__vector3XInput.move(10,160)
        
        vector3YLabel = QtWidgets.QLabel("Y", self)
        vector3YLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3YLabel.resize(150,20)
        vector3YLabel.move(170,140)

        self.__vector3YInput = QtWidgets.QLineEdit(self)
        self.__vector3YInput.resize(150, 20)
        self.__vector3YInput.move(170,160)
        
        vector3ZLabel = QtWidgets.QLabel("Z", self)
        vector3ZLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3ZLabel.resize(150,20)
        vector3ZLabel.move(330,140)

        self.__vector3YInput = QtWidgets.QLineEdit(self)
        self.__vector3YInput.resize(150, 20)
        self.__vector3YInput.move(330,160)
        
        self.__updateButton = QtWidgets.QPushButton("Update", self)
        self.__updateButton.resize(470, 20)
        self.__updateButton.move(10, 190)

        # add graph plot
        self.__graphPlot = graphicalPlot(self)
        self.__graphPlot.move(10,220)
        self.__graphPlot.resize(470,470)
    
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
        #self.__graphAxis.cla()

        #self.__graphAxis.quiver()

        plt.show()

# main entry point
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())