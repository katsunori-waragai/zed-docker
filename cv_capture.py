import cv2

def main():
    capture = cv2.VideoCapture(0)
    i = 0 
    while True:
        r, data = capture.read()
        if r:
            i = i + 1
            cv2.imshow("image", data)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()
