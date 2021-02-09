import cv2


class Camera:
    def __init__(self, camIdx, width, height):
        self.camera = cv2.VideoCapture(camIdx)
        self.width = width
        self.height = height

    def capture(self):
        _, frame = self.camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # set image center
        h, w = frame.shape[:2]
        mid_y = h // 2
        mid_x = w // 2

        # adjust image dimension
        rRes = self.width / self.height
        r = w / h

        if r > rRes:
            w = int(h * rRes)
        elif r < rRes:
            h = int(w / rRes)

        # set crop area
        y1 = mid_y - h // 2
        y2 = mid_y + h // 2
        x1 = mid_x - w // 2
        x2 = mid_x + w // 2

        frame = frame[y1:y2, x1:x2]
        displayFrame = cv2.resize(frame, (self.width, self.height))

        return frame, displayFrame

