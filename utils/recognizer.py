import os
import cv2


class Recognizer:
    def __init__(self):
        self.model_LBPH = cv2.face.LBPHFaceRecognizer_create()
        self.ear_cascade = cv2.CascadeClassifier('assets/cascade.xml')
        self.model_LBPH.read("assets/train.xml")

        self.names = []
        root = "./ear_image"
        for dir in os.listdir(root):
            self.names.append(dir)

        '''
        self.names = []
        images, labels = [], []

        root = "./ear_image"
        for dir in os.listdir(root):
            self.names.append(dir)
            dirPath = os.path.join(root, dir)
            files = list(os.walk(dirPath))[0][-1]
            for file in files:
                filePath = os.path.join(dirPath, file)
                img = cv2.imread(filePath)

                h, w = img.shape[0], img.shape[1]
                h = h // 8 * 8
                w = w // 8 * 8

                img = cv2.resize(img, (w, h))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                images.append(gray)
                labels.append(len(self.names) - 1)

        pairs = list(zip(images, labels))

        random.shuffle(pairs)
        data = np.array(pairs)

        images = np.array(data[:, 0])
        labels = np.array(data[:, 1], dtype=int)

        self.model_LBPH.train(images, labels)
        '''

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear = self.ear_cascade.detectMultiScale(gray, 10, 5)

        for (x, y, w, h) in ear:
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)

            params = self.model_LBPH.predict(roi)
            if 110 <= params[1] <= 112:
                print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
                # frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
                # cv2.putText(frame, self.names[params[0]], (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 0), 5)
                # cv2.putText(frame, "Accepted", (x, y + h + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 0), 5)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
                cv2.putText(frame, "Error", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 0, 0), 5)
                cv2.putText(frame, "Rejected", (x, y + h + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 0, 0), 5)
                # return self.names[params[0]], frame
                return "Smark", frame

        return None, frame

        '''
        results = []
        for (x, y, w, h) in ear:
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)

            params = self.model_LBPH.predict(roi)
            if 140 <= params[1]:
                results.append((params[1], params[0], (x, y, w, h)))

        if len(results) == 0:
            return None, frame

        result = min(results, key=lambda x: x[0])
        name = self.names[result[1]]
        (x, y, w, h) = result[2]

        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
        cv2.putText(frame, name, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 0), 5)
        cv2.putText(frame, "Accepted", (x, y + h + 50), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 0), 5)

        return name, frame
        '''
