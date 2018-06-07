import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore, QtGui
import math

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
        vector1HeadingLabel.setStyleSheet('color: red')
        vector1HeadingLabel.resize(490, 20)
        vector1HeadingLabel.move(0,0)

        self.__vector1Show = QtWidgets.QCheckBox("Show", self)
        self.__vector1Show.resize(50, 20)
        self.__vector1Show.move(440,0)

        vector1XLabel = QtWidgets.QLabel("X", self)
        vector1XLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1XLabel.resize(150,20)
        vector1XLabel.move(10,20)

        validator = QtGui.QDoubleValidator()

        self.__vector1XInputA = QtWidgets.QLineEdit(self)
        self.__vector1XInputA.setValidator(validator)
        self.__vector1XInputA.resize(70, 20)
        self.__vector1XInputA.move(10,40)
        
        self.__vector1XInputB = QtWidgets.QLineEdit(self)
        self.__vector1XInputB.setValidator(validator)
        self.__vector1XInputB.resize(70, 20)
        self.__vector1XInputB.move(90,40)
        
        vector1YLabel = QtWidgets.QLabel("Y", self)
        vector1YLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1YLabel.resize(150,20)
        vector1YLabel.move(170,20)

        self.__vector1YInputA = QtWidgets.QLineEdit(self)
        self.__vector1YInputA.setValidator(validator)
        self.__vector1YInputA.resize(70, 20)
        self.__vector1YInputA.move(170,40)
        
        self.__vector1YInputB = QtWidgets.QLineEdit(self)
        self.__vector1YInputB.setValidator(validator)
        self.__vector1YInputB.resize(70, 20)
        self.__vector1YInputB.move(250,40)
        
        vector1ZLabel = QtWidgets.QLabel("Z", self)
        vector1ZLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1ZLabel.resize(150,20)
        vector1ZLabel.move(330,20)

        self.__vector1ZInputA = QtWidgets.QLineEdit(self)
        self.__vector1ZInputA.setValidator(validator)
        self.__vector1ZInputA.resize(70, 20)
        self.__vector1ZInputA.move(330,40)

        self.__vector1ZInputB = QtWidgets.QLineEdit(self)
        self.__vector1ZInputB.setValidator(validator)
        self.__vector1ZInputB.resize(70, 20)
        self.__vector1ZInputB.move(410,40)

        # vector 2
        vector2HeadingLabel = QtWidgets.QLabel("Vector 2", self)
        vector2HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2HeadingLabel.setStyleSheet('color: green')
        vector2HeadingLabel.resize(490, 20)
        vector2HeadingLabel.move(0,60)

        self.__vector2Show = QtWidgets.QCheckBox("Show", self)
        self.__vector2Show.resize(50, 20)
        self.__vector2Show.move(440,60)

        vector2XLabel = QtWidgets.QLabel("X", self)
        vector2XLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2XLabel.resize(150,20)
        vector2XLabel.move(10,80)

        self.__vector2XInputA = QtWidgets.QLineEdit(self)
        self.__vector2XInputA.setValidator(validator)
        self.__vector2XInputA.resize(70, 20)
        self.__vector2XInputA.move(10,100)

        self.__vector2XInputB = QtWidgets.QLineEdit(self)
        self.__vector2XInputB.setValidator(validator)
        self.__vector2XInputB.resize(70, 20)
        self.__vector2XInputB.move(90,100)
        
        vector2YLabel = QtWidgets.QLabel("Y", self)
        vector2YLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2YLabel.resize(150,20)
        vector2YLabel.move(170,80)

        self.__vector2YInputA = QtWidgets.QLineEdit(self)
        self.__vector2YInputA.setValidator(validator)
        self.__vector2YInputA.resize(70, 20)
        self.__vector2YInputA.move(170,100)
        
        self.__vector2YInputB = QtWidgets.QLineEdit(self)
        self.__vector2YInputB.setValidator(validator)
        self.__vector2YInputB.resize(70, 20)
        self.__vector2YInputB.move(250,100)
        
        vector2ZLabel = QtWidgets.QLabel("Z", self)
        vector2ZLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2ZLabel.resize(150,20)
        vector2ZLabel.move(330,80)

        self.__vector2ZInputA = QtWidgets.QLineEdit(self)
        self.__vector2ZInputA.setValidator(validator)
        self.__vector2ZInputA.resize(70, 20)
        self.__vector2ZInputA.move(330,100)
        
        self.__vector2ZInputB = QtWidgets.QLineEdit(self)
        self.__vector2ZInputB.setValidator(validator)
        self.__vector2ZInputB.resize(70, 20)
        self.__vector2ZInputB.move(410,100)
        
        # vector 3 
        vector3HeadingLabel = QtWidgets.QLabel("Vector 3", self)
        vector3HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3HeadingLabel.setStyleSheet('color: blue')
        vector3HeadingLabel.resize(490, 20)
        vector3HeadingLabel.move(0,120)

        self.__vector3Show = QtWidgets.QCheckBox("Show", self)
        self.__vector3Show.resize(50, 20)
        self.__vector3Show.move(440,120)

        vector3XLabel = QtWidgets.QLabel("X", self)
        vector3XLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3XLabel.resize(150,20)
        vector3XLabel.move(10,140)

        self.__vector3XInputA = QtWidgets.QLineEdit(self)
        self.__vector3XInputA.setValidator(validator)
        self.__vector3XInputA.resize(70, 20)
        self.__vector3XInputA.move(10,160)

        self.__vector3XInputB = QtWidgets.QLineEdit(self)
        self.__vector3XInputB.setValidator(validator)
        self.__vector3XInputB.resize(70, 20)
        self.__vector3XInputB.move(90,160)
        
        vector3YLabel = QtWidgets.QLabel("Y", self)
        vector3YLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3YLabel.resize(150,20)
        vector3YLabel.move(170,140)

        self.__vector3YInputA = QtWidgets.QLineEdit(self)
        self.__vector3YInputA.setValidator(validator)
        self.__vector3YInputA.resize(70, 20)
        self.__vector3YInputA.move(170,160)
        
        self.__vector3YInputB = QtWidgets.QLineEdit(self)
        self.__vector3YInputB.setValidator(validator)
        self.__vector3YInputB.resize(70, 20)
        self.__vector3YInputB.move(250,160)
        
        vector3ZLabel = QtWidgets.QLabel("Z", self)
        vector3ZLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3ZLabel.resize(150,20)
        vector3ZLabel.move(330,140)

        self.__vector3ZInputA = QtWidgets.QLineEdit(self)
        self.__vector3ZInputA.setValidator(validator)
        self.__vector3ZInputA.resize(70, 20)
        self.__vector3ZInputA.move(330,160)
        
        self.__vector3ZInputB = QtWidgets.QLineEdit(self)
        self.__vector3ZInputB.setValidator(validator)
        self.__vector3ZInputB.resize(70, 20)
        self.__vector3ZInputB.move(410,160)
        
        self.__updateButton = QtWidgets.QPushButton("Update", self)
        self.__updateButton.resize(470, 20)
        self.__updateButton.move(10, 190)
        self.__updateButton.clicked.connect(self.__updateGraph)

        # add graph plot
        self.__graphPlot = graphicalPlot(self)
        self.__graphPlot.move(10,220)
        self.__graphPlot.resize(470,470)
    
        # show the gui window
        self.show()
    
    def __updateGraph(self):
        vectors = []
        #
        # add the shown vectors to the vector list 
        if self.__vector1Show.isChecked():
            vectors.append([(float(self.__vector1XInputA.text()), 
                                float(self.__vector1YInputA.text()), 
                                float(self.__vector1ZInputA.text())),
                                (float(self.__vector1XInputB.text()), 
                                float(self.__vector1YInputB.text()), 
                                float(self.__vector1ZInputB.text())),
                                'r'])
        #
        if self.__vector2Show.isChecked():
            vectors.append([(float(self.__vector2XInputA.text()), 
                                float(self.__vector2YInputA.text()), 
                                float(self.__vector2ZInputA.text())),
                                (float(self.__vector2XInputB.text()), 
                                float(self.__vector2YInputB.text()), 
                                float(self.__vector2ZInputB.text())),
                                'g'])
        #
        if self.__vector3Show.isChecked():
            vectors.append([(float(self.__vector3XInputA.text()), 
                                float(self.__vector3YInputA.text()), 
                                float(self.__vector3ZInputA.text())),
                                (float(self.__vector3XInputB.text()), 
                                float(self.__vector3YInputB.text()), 
                                float(self.__vector3ZInputB.text())),
                                'b'])
        #  
        # update the graph plot with the shown vectors
        self.__graphPlot.updateGraph(vectors)
    

# Graph class deals with showing the vector graph
class graphicalPlot(FigureCanvas):

    # graphicalPlot class constructor
    def __init__(self, parent=None, width=100, height=50, dpi=100):
        
        # create a figure
        fig = Figure(figsize=(width,height), dpi=dpi)

        # set up the figure canvas
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, 
                                    QtWidgets.QSizePolicy.Expanding, 
                                    QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # create an axis with 3D projection
        self.__graphAxis = fig.add_subplot(111, projection='3d')

        # show the plot
        plt.show()
    
    # public method to update the graph
    def updateGraph(self, vectors):
        # clear the graph axis
        self.__graphAxis.cla()
        #
        # min and max values used for axis scaling
        max_values_set = False
        x_max = 0.0
        x_min = 0.0
        y_max = 0.0
        y_min = 0.0
        z_max = 0.0
        z_min = 0.0
        #
        # loop through all vectors 
        for vect in vectors:
            # determine the min and max axis values
            if False == max_values_set:
                x_max = max(vect[0][0], vect[1][0])
                x_min = min(vect[0][0], vect[1][0])
                y_max = max(vect[0][1], vect[1][1])
                y_min = min(vect[0][1], vect[1][1])
                z_max = max(vect[0][2], vect[1][2])
                z_min = min(vect[0][2], vect[1][2])
                #
                max_values_set = True
            else:
                x_max = max(vect[0][0], vect[1][0], x_max)
                x_min = min(vect[0][0], vect[1][0], x_min)
                y_max = max(vect[0][1], vect[1][1], y_max)
                y_min = min(vect[0][1], vect[1][1], y_min)
                z_max = max(vect[0][2], vect[1][2], z_max)
                z_min = min(vect[0][2], vect[1][2], z_min)
            #
            # add the vector as a quiver with no arrow head
            self.__graphAxis.quiver(vect[0][0], 
                                    vect[0][1], 
                                    vect[0][2], 
                                    (vect[1][0] - vect[0][0]), 
                                    (vect[1][1] - vect[0][1]), 
                                    (vect[1][2] - vect[0][2]), 
                                    color=vect[2],
                                    arrow_length_ratio=0)
        #
        # if a vector has been added then the max_values_set will be true so update the axis limits
        if(True == max_values_set):
            self.__graphAxis.set_xlim([x_min, x_max])
            self.__graphAxis.set_xlabel('x')
            self.__graphAxis.set_ylim([y_min, y_max])
            self.__graphAxis.set_ylabel('y')
            self.__graphAxis.set_zlim([z_min, z_max])
            self.__graphAxis.set_zlabel('z')
            self.__graphAxis.set_title('vector plot')
        # 
        # draw the graph
        self.draw()
    
# main entry point
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())