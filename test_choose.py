import sys
from PyQt5.QtWidgets import QApplication

from utils.choose import Window


# create variables for running window
app = QApplication(sys.argv)
w = Window()

# w.processFrame()

# display window
w.show()
sys.exit(app.exec_())
