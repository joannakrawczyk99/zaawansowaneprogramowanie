import time
import cv2
from detection.Detector import detect_person

if __name__ == "__main__":
    images = [cv2.imread('images/people1.jpg'), cv2.imread('images/people2.jpg'),
              cv2.imread('images/people3.jpg'), cv2.imread('images/people4.jpg')]
    for image in images:
        start_time = time.time()
        detect_person(image)
        print("--- %.3f sec ---" % (time.time() - start_time))
