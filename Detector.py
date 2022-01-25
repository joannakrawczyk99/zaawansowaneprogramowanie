import cv2
import imutils

model = cv2.HOGDescriptor()
model.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    cords, weights = model.detectMultiScale(frame,
                                            winStride=(4, 4),
                                            padding=(8, 8),
                                            scale=1.03)

    person = 1
    for x, y, w, h in cords:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        person += 1

    cv2.putText(frame,
                f'Total Persons : {person - 1}',
                (40, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 250, 100), 2)
    cv2.imshow('output', frame)
    return frame


def detect_image(image):
    image = imutils.resize(image, width=min(800, image.shape[1]))
    result_image = detect(image)
    cv2.imshow('output',result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_person(image_path):
    if image_path is not None:
        print('[INFO] Opening Image from path.')
        detect_image(image_path)
