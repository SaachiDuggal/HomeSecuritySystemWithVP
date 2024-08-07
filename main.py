import cv2
from datetime import datetime
import os
import glob

cap = cv2.VideoCapture(0)

mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, pre_frame = cap.read()
    gray = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)

    fgmask = mog.apply(gray)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < 1000:
            continue

        # Using CascadeClassifier from openCV to extract all the features from haarcascade.
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        check, frame = cap.read()

        # Converting the image into grayscale.
        if frame is not None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detecting for any face in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

            # Creating a square around the face, recording the date and time, and face detected image file name.
            for x, y, w, h in faces:
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                exact_time = datetime.now().strftime('%Y-%b-%d-%H-%M-%S-%f')
                cv2.imwrite("C:\\Users\\ASUS\\Desktop\\Photo output\\Temp_folder\\face_detected_" + str(
                    exact_time) + ".jpg", frame)

            # Displaying the frames of the video to the user.
            cv2.imshow("Home Surveillance", frame)
            key = cv2.waitKey(1)

            # If 'q' button pressed then the key triggered and storing of all the images as video.
            if key == ord('q'):
                # Path where images are present
                dir_path = "C:\\ADD\\THE\\PATH"
                output = "C:\\ANOTHER\\PATH " + str(exact_time) + ".mp4"

                # All the names of our image files
                images = [img for img in os.listdir(dir_path) if img.endswith(".jpg")]

                # Image path
                image_path = os.path.join(dir_path, images[0])
                frame = cv2.imread(image_path)
                height, width, _ = frame.shape

                # Specify the encoding of the video
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(output, fourcc, 5.0, (width, height))

                # Writing the images on a video file
                for image in images:
                    image_path = os.path.join(dir_path, image)
                    frame = cv2.imread(image_path)
                    out.write(frame)
                break

        # Releasing the video
        cap.release()

    cv2.destroyAllWindows()

    break
files = glob.glob('C:\\ADD\\THE\\PATH*')
for f in files:
    os.remove(f)
