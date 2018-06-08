from PyQt5 import QtCore, QtGui, QtWidgets
import graphicalPlot as graph

# main Gui class deals with showing the gui and responding to user input
class Gui(QtWidgets.QMainWindow):

    # Gui class constructor
    def __init__(self):
    
        super().__init__()

        self._initGui()

    def _initGui(self):

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

        self._vector1Show = QtWidgets.QCheckBox("Show", self)
        self._vector1Show.resize(50, 20)
        self._vector1Show.move(440,0)

        vector1FromLabel = QtWidgets.QLabel("From [x] [y] [z]", self)
        vector1FromLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1FromLabel.resize(245, 20)
        vector1FromLabel.move(0,20)

        vector1ToLabel = QtWidgets.QLabel("To [x] [y] [z]", self)
        vector1ToLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector1ToLabel.resize(245, 20)
        vector1ToLabel.move(245,20)

        validator = QtGui.QDoubleValidator()

        self._vector1XInputA = QtWidgets.QLineEdit(self)
        self._vector1XInputA.setValidator(validator)
        self._vector1XInputA.resize(70, 20)
        self._vector1XInputA.move(10,40)

        self._vector1YInputA = QtWidgets.QLineEdit(self)
        self._vector1YInputA.setValidator(validator)
        self._vector1YInputA.resize(70, 20)
        self._vector1YInputA.move(90,40)

        self._vector1ZInputA = QtWidgets.QLineEdit(self)
        self._vector1ZInputA.setValidator(validator)
        self._vector1ZInputA.resize(70, 20)
        self._vector1ZInputA.move(170,40)
                
        self._vector1XInputB = QtWidgets.QLineEdit(self)
        self._vector1XInputB.setValidator(validator)
        self._vector1XInputB.resize(70, 20)
        self._vector1XInputB.move(250,40)
        
        self._vector1YInputB = QtWidgets.QLineEdit(self)
        self._vector1YInputB.setValidator(validator)
        self._vector1YInputB.resize(70, 20)
        self._vector1YInputB.move(330,40)
        
        self._vector1ZInputB = QtWidgets.QLineEdit(self)
        self._vector1ZInputB.setValidator(validator)
        self._vector1ZInputB.resize(70, 20)
        self._vector1ZInputB.move(410,40)

        # vector 2
        vector2HeadingLabel = QtWidgets.QLabel("Vector 2", self)
        vector2HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2HeadingLabel.setStyleSheet('color: green')
        vector2HeadingLabel.resize(490, 20)
        vector2HeadingLabel.move(0,60)

        self._vector2Show = QtWidgets.QCheckBox("Show", self)
        self._vector2Show.resize(50, 20)
        self._vector2Show.move(440,60)

        vector2FromLabel = QtWidgets.QLabel("From [x] [y] [z]", self)
        vector2FromLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2FromLabel.resize(245, 20)
        vector2FromLabel.move(0,80)

        vector2ToLabel = QtWidgets.QLabel("To [x] [y] [z]", self)
        vector2ToLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector2ToLabel.resize(245, 20)
        vector2ToLabel.move(245,80)

        self._vector2XInputA = QtWidgets.QLineEdit(self)
        self._vector2XInputA.setValidator(validator)
        self._vector2XInputA.resize(70, 20)
        self._vector2XInputA.move(10,100)

        self._vector2YInputA = QtWidgets.QLineEdit(self)
        self._vector2YInputA.setValidator(validator)
        self._vector2YInputA.resize(70, 20)
        self._vector2YInputA.move(90,100)

        self._vector2ZInputA = QtWidgets.QLineEdit(self)
        self._vector2ZInputA.setValidator(validator)
        self._vector2ZInputA.resize(70, 20)
        self._vector2ZInputA.move(170,100)

        self._vector2XInputB = QtWidgets.QLineEdit(self)
        self._vector2XInputB.setValidator(validator)
        self._vector2XInputB.resize(70, 20)
        self._vector2XInputB.move(250,100)
                
        self._vector2YInputB = QtWidgets.QLineEdit(self)
        self._vector2YInputB.setValidator(validator)
        self._vector2YInputB.resize(70, 20)
        self._vector2YInputB.move(330,100)

        self._vector2ZInputB = QtWidgets.QLineEdit(self)
        self._vector2ZInputB.setValidator(validator)
        self._vector2ZInputB.resize(70, 20)
        self._vector2ZInputB.move(410,100)
        
        # vector 3 
        vector3HeadingLabel = QtWidgets.QLabel("Vector 3", self)
        vector3HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3HeadingLabel.setStyleSheet('color: blue')
        vector3HeadingLabel.resize(490, 20)
        vector3HeadingLabel.move(0,120)

        self._vector3Show = QtWidgets.QCheckBox("Show", self)
        self._vector3Show.resize(50, 20)
        self._vector3Show.move(440,120)

        vector3FromLabel = QtWidgets.QLabel("From [x] [y] [z]", self)
        vector3FromLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3FromLabel.resize(245, 20)
        vector3FromLabel.move(0,140)

        vector3ToLabel = QtWidgets.QLabel("To [x] [y] [z]", self)
        vector3ToLabel.setAlignment(QtCore.Qt.AlignCenter)
        vector3ToLabel.resize(245, 20)
        vector3ToLabel.move(245,140)

        self._vector3XInputA = QtWidgets.QLineEdit(self)
        self._vector3XInputA.setValidator(validator)
        self._vector3XInputA.resize(70, 20)
        self._vector3XInputA.move(10,160)

        self._vector3YInputA = QtWidgets.QLineEdit(self)
        self._vector3YInputA.setValidator(validator)
        self._vector3YInputA.resize(70, 20)
        self._vector3YInputA.move(90,160)
        
        self._vector3ZInputA = QtWidgets.QLineEdit(self)
        self._vector3ZInputA.setValidator(validator)
        self._vector3ZInputA.resize(70, 20)
        self._vector3ZInputA.move(170,160)

        self._vector3XInputB = QtWidgets.QLineEdit(self)
        self._vector3XInputB.setValidator(validator)
        self._vector3XInputB.resize(70, 20)
        self._vector3XInputB.move(250,160)
                
        self._vector3YInputB = QtWidgets.QLineEdit(self)
        self._vector3YInputB.setValidator(validator)
        self._vector3YInputB.resize(70, 20)
        self._vector3YInputB.move(330,160)
        
        self._vector3ZInputB = QtWidgets.QLineEdit(self)
        self._vector3ZInputB.setValidator(validator)
        self._vector3ZInputB.resize(70, 20)
        self._vector3ZInputB.move(410,160)
        
        self._updateButton = QtWidgets.QPushButton("Update", self)
        self._updateButton.resize(470, 20)
        self._updateButton.move(10, 190)
        self._updateButton.clicked.connect(self._updateGraph)

        # add graph plot
        self._graphPlot = graph.graphicalPlot(self)
        self._graphPlot.move(10,220)
        self._graphPlot.resize(470,470)
    
        # show the gui window
        self.show()
    
    def _updateGraph(self):
        vectors = []
        #
        # add the shown vectors to the vector list 
        if self._vector1Show.isChecked():
            vectors.append([(float(self._vector1XInputA.text()), 
                                float(self._vector1YInputA.text()), 
                                float(self._vector1ZInputA.text())),
                                (float(self._vector1XInputB.text()), 
                                float(self._vector1YInputB.text()), 
                                float(self._vector1ZInputB.text())),
                                'r'])
        #
        if self._vector2Show.isChecked():
            vectors.append([(float(self._vector2XInputA.text()), 
                                float(self._vector2YInputA.text()), 
                                float(self._vector2ZInputA.text())),
                                (float(self._vector2XInputB.text()), 
                                float(self._vector2YInputB.text()), 
                                float(self._vector2ZInputB.text())),
                                'g'])
        #
        if self._vector3Show.isChecked():
            vectors.append([(float(self._vector3XInputA.text()), 
                                float(self._vector3YInputA.text()), 
                                float(self._vector3ZInputA.text())),
                                (float(self._vector3XInputB.text()), 
                                float(self._vector3YInputB.text()), 
                                float(self._vector3ZInputB.text())),
                                'b'])
        #  
        # update the graph plot with the shown vectors
        self._graphPlot.updateGraph(vectors)
