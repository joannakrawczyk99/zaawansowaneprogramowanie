import cv2
import imutils

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    cords, weights = HOGCV.detectMultiScale(frame,
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
                cv2.FONT_HERSHEY_DUPLEX,
                0.8,
                (255, 0, 0), 2)
    cv2.imshow('output', frame)
    return frame


def detect_person(args):
    image_path = args["image"]
    if image_path is not None:
        print('[INFO] Opening Image from path.')
        detect_image(image_path, args['output'])


def detect_image(path, output_path):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(800, image.shape[1]))
    result_image = detect(image)
    if output_path is not None:
        cv2.imwrite(output_path, result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()