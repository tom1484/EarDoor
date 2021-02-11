import time
import base64
import io
from imageio import imread
from datetime import datetime

from PyQt5.QtGui import QImage, QPixmap


class Updater:
    def __init__(self, ui, db, slm):
        self.ui = ui
        self.db = db
        self.slm = slm

        self.time = -10

    def update(self, name, frame):
        if time.time() - self.time > 5:
            self.updateFrame(frame)
            self.clearIdentity()
            if name is not None:
                self.updateIdentity(name)
                self.time = time.time()

    def clearIdentity(self):
        # clear information
        self.ui.name.setText('')
        self.ui.time.setText('')
        self.ui.location.setText('')

        self.slm.setStringList([])

        # clear image
        self.ui.picture.setPixmap(QPixmap())

    def updateIdentity(self, name):
        # update information
        now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        self.db.add_record(name, now)

        self.ui.name.setText(name)
        self.ui.time.setText(now)
        self.ui.location.setText("NTNU")

        records = self.db.select_records(name)
        self.slm.setStringList(records)

        # update image
        raw = self.db.select_image(name)
        img = imread(io.BytesIO(base64.b64decode(raw)))

        img = QImage(img, img.shape[1], img.shape[0],
                     img.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        self.ui.picture.setPixmap(img)

    def updateFrame(self, frame):
        # convert image to QPixmap
        img = QImage(frame, frame.shape[1], frame.shape[0],
                     frame.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        # display image
        self.ui.camera.setPixmap(img)
        self.ui.camera.setScaledContents(True)
