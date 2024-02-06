########################################################################
#
# Copyright (c) 2022, STEREOLABS.
#
# All rights reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
########################################################################

import inspect
from pprint import pprint

import pyzed.sl as sl

import cv2

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
    depth_image = sl.Mat()
    runtime_parameters = sl.RuntimeParameters()
    while i < 50:
        # Grab an image, a RuntimeParameters object must be given to grab()
        if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
            # A new image is available if grab() returns SUCCESS
            zed.retrieve_image(image, sl.VIEW.LEFT)
            zed.retrieve_image(depth_image, sl.VIEW.DEPTH)
            timestamp = zed.get_timestamp(sl.TIME_REFERENCE.CURRENT)  # Get the timestamp at the time the image was captured
            print("Image resolution: {0} x {1} || Image timestamp: {2}\n".format(image.get_width(), image.get_height(),
                  timestamp.get_milliseconds()))
            i = i + 1
            print(f"{image=}")
            pprint(inspect.getmembers(image))
            print(f"{image.get_data()=}")
            data = image.get_data()  # 戻り値が配列になる。
            print(f"{image.get_data_type()=}")
            print(f"{image.get_channels()=}")
            print(f"{image.get_height()=}")
            print(f"{image.get_width()=}")
            print(f"{image.get_infos()=}")

            print(f"{depth_image.get_data_type()=}")
            print(f"{depth_image.get_channels()=}")
            print(f"{depth_image.get_height()=}")
            print(f"{depth_image.get_width()=}")
            print(f"{depth_image.get_infos()=}")

            depth_data = depth_image.get_data()
            cv2.imshow("zed2", data)
            cv2.imshow("zed2 depth", depth_data)
            key = cv2.waitKey(-1)
            if key & 0xff == ord('q'):
                break

    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()
