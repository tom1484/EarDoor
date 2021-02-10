import os
import cv2
import numpy as np
import random


class Recognizer:
    def __init__(self):
        self.model_LBPH = cv2.face.LBPHFaceRecognizer_create()
        self.ear_cascade = cv2.CascadeClassifier('assets/cascade.xml')
        self.model_LBPH.read("assets/train.xml")

        self.names = []
        images, labels = [], []

        root = "./ear_image"
        for dir in os.listdir(root):
            self.names.append(dir)
            # dirPath = os.path.join(root, dir)
            # files = list(os.walk(dirPath))[0][-1]
            # for file in files:
            #     filePath = os.path.join(dirPath, file)
            #     img = cv2.imread(filePath)
            #
            #     h, w = img.shape[0], img.shape[1]
            #     h = h // 8 * 8
            #     w = w // 8 * 8
            #
            #     img = cv2.resize(img, (w, h))
            #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #     images.append(gray)
            #     labels.append(len(self.names) - 1)
            #
            #     # ears = self.ear_cascade.detectMultiScale(gray, 10, 5)
            #     # for (x, y, w, h) in ears:
            #     #     crop = gray[y:y + h, x:x + w]
            #     #     images.append(crop)
            #     #     labels.append(len(self.names) - 1)
        #
        # pairs = list(zip(images, labels))
        #
        # random.shuffle(pairs)
        # data = np.array(pairs)
        #
        # images = np.array(data[:, 0])
        # labels = np.array(data[:, 1], dtype=int)
        #
        # self.model_LBPH.train(images, labels)

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear = self.ear_cascade.detectMultiScale(gray, 10, 5)

        for (x, y, w, h) in ear:
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)

            params = self.model_LBPH.predict(roi)
            if params[1] > 110:
                print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, self.names[params[0]], (x, y - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                return self.names[params[0]], frame

        return None, frame
