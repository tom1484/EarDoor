from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer, QStringListModel

from utils.window_ui import Ui_Form
from utils.recognizer import Recognizer
from utils.camera import Camera
from utils.database import Database
from utils.updater import Updater


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        db = Database(host='localhost', database='eardoor',
                      user='eardoor', password='14841484', table='records')
        slm = QStringListModel()

        self.ui.records.setModel(slm)
        self.updater = Updater(self.ui, db, slm)

        self.camera = Camera(1, self.ui.frame.width(), self.ui.frame.height())
        self.recognizer = Recognizer()

        self.fps = 50
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 // self.fps)

    def update(self):
        frame = self.camera.capture()
        name, frame = self.recognizer.detect(frame)
        self.updater.update(name, frame)
