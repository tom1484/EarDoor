from PyQt5.QtWidgets import QDialog

from utils.choose_ui import Ui_Form


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
