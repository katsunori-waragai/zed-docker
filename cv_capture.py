"""
SEE ALSO:
https://www.stereolabs.com/docs/depth-sensing/using-depth

https://github.com/stereolabs/zed-sdk/tree/master/tutorials/tutorial%203%20-%20depth%20sensing/python

https://stackoverflow.com/questions/67678048/whats-the-proper-way-to-colorize-a-16-bit-depth-image
"""

import inspect
from pprint import pprint


import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create a Camera object
    capture = cv2.VideoCapture(0)
    i = 0 
    while True:
        # Grab an image, a RuntimeParameters object must be given to grab()

        if 1:
            r, data = capture.read()
            # A new image is available if grab() returns SUCCESS
            i = i + 1
            # print(f"{image=}")
            cv2.imshow("image", data)
            cv2.waitKey(1)


    # Close the camera


if __name__ == "__main__":
    main()
