"""main_window_ui.py: ELEBAC22 Control system Main Window UI code."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2021, ELE320"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

from socket_client import *
from abstract_storage import *
from defines import *

from PyQt5 import QtWidgets, uic, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from random import randint
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self, ui_file, current_data: abstract_storage, connection: tuple[str, int], fullscreen):
        self.current_data = current_data
        self.connection_details = connection

        self.app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication

        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(ui_file, self) # Load the .ui file

        ## Map all used GUI Controls
        self.txt_dist = [
            self.findChild(QtWidgets.QLabel, 'dist_b_l'), 
            self.findChild(QtWidgets.QLabel, 'dist_b_r'),
            self.findChild(QtWidgets.QLabel, 'dist_f_l'), 
            self.findChild(QtWidgets.QLabel, 'dist_f_r')
            ]
        self.txt_motor = [self.findChild(QtWidgets.QTextBrowser, 'txt_motor_1'), self.findChild(QtWidgets.QTextBrowser, 'txt_motor_2')],
        self.txt_rotate = self.findChild(QtWidgets.QTextBrowser, 'txt_turn_angle')

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        self.socket_conn = socket_client(self.current_data, self.connection_details)
        self.socket_conn.start()
        self.update_plot_data()

        if fullscreen: 
            self.showFullScreen()
        self.show()
        self.app.exec_()

    def update_plot_data(self):
        data = self.current_data.get_recent_sensor_data()
        for row in data:
            if (row[0] >= 0 and row[0] < 4):
                self.txt_dist[row[0]].setText(str(row[2]))
