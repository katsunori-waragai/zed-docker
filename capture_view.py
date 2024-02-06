"""
SEE ALSO:
https://www.stereolabs.com/docs/depth-sensing/using-depth
"""

import inspect
from pprint import pprint

import pyzed.sl as sl

import cv2
import matplotlib.pyplot as plt

def main():
    # Create a Camera object
    zed = sl.Camera()

    # Create a InitParameters object and set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.AUTO # Use HD720 opr HD1200 video mode, depending on camera type.
    init_params.camera_fps = 30  # Set fps at 30

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print("Camera Open : "+repr(err)+". Exit program.")
        exit()


    # Capture 50 frames and stop
    i = 0
    image = sl.Mat()
    depth_map = sl.Mat()

    pprint(inspect.getmembers(image))  # sl.Mat() object のデータメンバーを表示させる。

    runtime_parameters = sl.RuntimeParameters()
    while i < 50:
        # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # A new image is available if grab() returns SUCCESS
            zed.retrieve_image(image, sl.VIEW.LEFT)
            zed.retrieve_measure(depth_map, sl.MEASURE.DEPTH) # Retrieve depth
            timestamp = zed.get_timestamp(sl.TIME_REFERENCE.CURRENT)  # Get the timestamp at the time the image was captured
            print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(image.get_width(), image.get_height(),
                  timestamp.get_milliseconds()))
            i = i + 1
            print(f"{image=}")
            print(f"{image.get_data()=}")
            data = image.get_data()  # 戻り値が配列になる。
            data = cv2.cvtColor(data, cv2.COLOR_BGRA2RGBA)
            print(f"{image.get_data_type()=}")
            print(f"{image.get_channels()=}")
            print(f"{image.get_height()=}")
            print(f"{image.get_width()=}")
            print(f"{image.get_infos()=}")

            depth_map_data = depth_map.get_data()
            print(f"{depth_map_data.shape=}")
            print(f"{depth_map_data.dtype=}")
            plt.figure(1)
            plt.subplot(1, 2, 1)
            plt.imshow(data)
            plt.subplot(1, 2, 2)
            plt.imshow(depth_map_data, cmap="jet")
            plt.draw()
            plt.pause(0.01)

            # cv2.imshow("zed2", data)
            # cv2.imshow("zed2 depth", depth_data)
            # key = cv2.waitKey(-1)
            # if key & 0xff == ord('q'):
            #     break

    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()
