import sys

vision_enabled = False
try:
    import cv2
    vision_enabled = True
except Exception as e:
    print("Warning: OpenCV not installed. To use facial recognition, make sure you've properly configured OpenCV.")


class Vision(object):
    def __init__(self, facial_recognition_model="models/facial_recognition_model.xml", camera=0):
        self.facial_recognition_model = facial_recognition_model
        self.camera = camera

    def recognize_face(self):
        """
        Wait until a face is recognized. If openCV is configured, always return true
        :return:
        """

        if vision_enabled is False:  # if opencv is not able to be imported, always return True
            return True

        face_cascade = cv2.CascadeClassifier(self.facial_recognition_model)
        video_capture = cv2.VideoCapture(self.camera)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )

            if len(faces) > 0:
                # When everything is done, release the capture
                video_capture.release()
                cv2.destroyAllWindows()

                return True


if __name__ == "__main__":
    faceCascade = cv2.CascadeClassifier("models/facial_recognition_model.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()