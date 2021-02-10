from datetime import datetime
import time


class IdentityUpdater:
    def __init__(self, ui, db, slm):
        self.ui = ui
        self.db = db
        self.slm = slm

        self.time = -10

    def update(self, name):
        if time.time() - self.time < 20:
            return

        now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        self.db.add_record(name, now)

        self.ui.name.setText(name)
        self.ui.time.setText(now)
        self.ui.location.setText("NTNU")

        records = self.db.select(name)
        self.slm.setStringList(records)

        self.time = time.time()
