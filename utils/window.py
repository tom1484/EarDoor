from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer, QStringListModel, Qt
from PyQt5.QtGui import QImage, QPixmap

from utils.window_ui import Ui_Form
from utils.recognizer import Recognizer
from utils.camera import Camera
from utils.database import Database
from utils.identity_updater import IdentityUpdater


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        db = Database(host='localhost', database='eardoor',
                      user='eardoor', password='14841484', table='records')
        slm = QStringListModel()

        self.ui.records.setModel(slm)
        self.identity_updater = IdentityUpdater(self.ui, db, slm)

        self.camera = Camera(1, self.ui.frame.width(), self.ui.frame.height())
        self.recognizer = Recognizer()

        self.fps = 50
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.processFrame)
        self.timer.start(1000 // self.fps)

    def processFrame(self):
        frame = self.camera.capture()
        name, frame = self.recognizer.detect(frame)

        if name is not None:
            self.identity_updater.update(name)

        # convert image to QPixmap
        img = QImage(frame, frame.shape[1], frame.shape[0],
                     frame.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        # display image
        self.ui.frame.setPixmap(img)
        self.ui.frame.setScaledContents(True)

