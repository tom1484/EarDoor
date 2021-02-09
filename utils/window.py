from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QTimer, QStringListModel
from PyQt5.QtGui import QImage, QPixmap

from utils.window_ui import Ui_Form
from utils.recognizer import Recognizer
from utils.camera import Camera


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.camera = Camera(0, self.ui.frame.width(), self.ui.frame.height())
        self.recognizer = Recognizer()

        self.fps = 30
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.processFrame)
        self.timer.start(1000 // self.fps)

        # slm = QStringListModel()
        # qList = ['Item1', 'Item2']
        # slm.setStringList(qList)
        # self.ui.record.setModel(slm)

    def processFrame(self):
        frame, displayFrame = self.camera.capture()
        frame = self.recognizer.detect(frame, displayFrame)

        # convert image to QPixmap
        img = QImage(frame, frame.shape[1], frame.shape[0],
                     frame.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        # display image
        self.ui.frame.setPixmap(img)
        self.ui.frame.setScaledContents(True)

