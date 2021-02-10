import sys
from PyQt5.QtWidgets import QApplication

from utils.window import Window
from utils.database import Database

# DB = Database(host='localhost', database='eardoor',
#               user='eardoor', password='14841484', table='records')

# create variables for running window
app = QApplication(sys.argv)
w = Window()

# w.processFrame()

# display window
w.show()
sys.exit(app.exec_())
