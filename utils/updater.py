from datetime import datetime
import time

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
            if name is not None:
                self.updateIdentity(name)
                self.time = time.time()

    def updateIdentity(self, name):
        now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        self.db.add_record(name, now)

        self.ui.name.setText(name)
        self.ui.time.setText(now)
        self.ui.location.setText("NTNU")

        records = self.db.select(name)
        self.slm.setStringList(records)

    def updateFrame(self, frame):
        # convert image to QPixmap
        img = QImage(frame, frame.shape[1], frame.shape[0],
                     frame.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        # display image
        self.ui.frame.setPixmap(img)
        self.ui.frame.setScaledContents(True)
