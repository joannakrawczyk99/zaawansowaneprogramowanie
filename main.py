import cv2
from Detector import detect_person
from Parser import argsParser

if __name__ == "__main__":
    args = argsParser()
    detect_person(args)