# zed-docker
docker example for zed sdk (stereolabs) on Jetson


## Direct install of ZED SDK
- 直接 ZED SDKをインストール

### 実行結果例
zed-sdk/body tracking/body tracking/python$ python3 body_tracking.py 


![](fig/body_tracking_python.png)

object detection/image viewer/python$ python3 object_detection_image_viewer.py 

![](fig/object_detection_image_viewer.png)

object detection/birds eye viewer/python$ python3 object_detection_birds_view.py
![](fig/object_detection_birds_view.png)
## install ZED SDK using Docker


### 以下のdocker hub から該当するtagを見つけること
https://hub.docker.com/r/stereolabs/zed/

### JetPack5.1
- JetPack の場合はUbuntuPCとはtagのルールが異なる。

export TAGS=4.0-py-devel-jetson-jp5.1.0
sudo docker pull stereolabs/zed:${TAGS}


sudo docker run -it --privileged  stereolabs/zed:${TAGS}


docker pull stereolabs/zed:3.7-gl-devel-cuda11.4-ubuntu20.04  # pull ZED SDK v3.7.x devel release with OpenGL support under Ubuntu 20.04
xhost +si:localuser:root  # allow containers to communicate with X server
  docker run -it --runtime nvidia --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix stereolabs/zed:3.7-gl-devel-cuda11.4-ubuntu20.04


Q: g++ が見つからない
```
sudo apt update
sudo apt install build-essential
```

Q: /usr/local/zed/samplesはどこ？

```
  apt update && apt install cmake -y
  cp -r /usr/local/zed/samples/depth\ sensing/ /tmp/depth-sensing
  cd /tmp/depth-sensing/cpp ; mkdir build ; cd build
  cmake .. && make
  ./ZED_Depth_Sensing
```

Q: CUDA_TOOLKIT_ROOT_DIR


Q: Docker環境の外
Docker環境の外
$ ls /usr/local/cuda
bin                EULA.txt  lib64  README   targets
compute-sanitizer  extras    nvml   samples  tools
DOCS               include   nvvm   share    version.json

Docker環境の内
ls /usr/local/cuda
include  lib64  targets
