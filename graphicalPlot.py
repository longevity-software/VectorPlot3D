import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from PyQt5 import QtWidgets


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
