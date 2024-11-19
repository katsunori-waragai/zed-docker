# zed-docker
docker example for zed sdk (stereolabs) on Jetson

## このリポジトリの目的
- ZED SDKのサンプルをDocker Imageに基づいて動作させるやり方への解説
- 理由：
  - Jetson上の環境を破壊することなく、安心してZED SDK をインストールして、ZED SDKのサンプルに親しむことを目的としている。
  - StereoLabsのZED カメラならびにZED SDKについての日本語情報は少ない。それを補うことを目的としている。
### このリポジトリが含まないもの
- ZED SDK やStereoLabsのカメラを用いた新規な実装。

## 動作環境
- NVIDIA Jetson AGX Orin
- Ubuntu
- python>=3.8
- Docker
### 移植可能なハードウェア
- Cudaデバイスが利用可能なPC（Windows, Ubuntu)
### 必須のハードウェア
ZED2, ZED2i, ZED-X などのStereoLabsのステレオカメラ

#### ZED SDKとは
1. インストラーでインストーされるSDK部分
2. GitHub にあるサンプルプログラム群　https://github.com/stereolabs/zed-sdk
この２つがある。
以下の記述の中ではZED SDKとしては、インストーラでインストールされるSDKの部分を指している。
## 1. SDKのインストール
#### 選択肢１：Direct install of ZED SDK
- 直接 ZED SDKをインストール
- また、Githubのzed-sdk のサンプルプログラムを仮想環境を使わずに直接インストール
　この場合、サンプルプログラムのインストール時に、環境を改変してしまうことで、他のアプリケーションが動作しなくなってしまう可能性が生じる。

#### 選択肢２：Docker image by StereoLabs
https://hub.docker.com/r/stereolabs/zed/tags

JetPack のバージョンに合わせたインストーラーをダウンロードする。
`ZED_SDK_Tegra_L4T35.2_v4.0.8.zstd.run`
インストーラーを実行する。

実際の作業
1. bash docker_build.sh
2. xhost +
3. bash docker_run.sh

Dockerの仮想環境が立ち上がる。

## ZED SDK /samplesのインストール
以下は、その仮想環境内で実施する。

```
git clone https://github.com/stereolabs/zed-sdk
```

それぞれのsample application の説明は、上記のgithub のリポジトリの各README.md に記載がある。

### 実行結果例
python　スクリプトは、容易に実行できる。

#### body tracking 人のポーズ推定でのtracking
zed-sdk/body tracking/body tracking/python$ python3 body_tracking.py



![](fig/body_tracking_python.png)

検出した人のボーンを表示します。
頭部については、鼻・両目・両耳の位置を表示します。

#### object detection での検出結果の表示
object detection/image viewer/python$ python3 object_detection_image_viewer.py

![](fig/object_detection_image_viewer.png)

物体検出の結果を3Dの検出枠で表示します。


#### object detectionでのbird_viewでの表示
object detection/birds eye viewer/python$ python3 object_detection_birds_view.py
![](fig/object_detection_birds_view.png)
図の右側に、検出された人の位置を表示している。

StereoLabsのカメラは以下の計測範囲です。
このカメラは焦点距離 2.1mm のを選択しているので、20m までが算出可能です「。

```commandline
Depth Range Max
0.3m to 20m (1ft to 65ft) with 2.1 mm lens
1.5m to 35m (4.9ft to 114.8ft) with 4 mm lens
```

#### positional tracking
- ZED2iには、IMUが内蔵されています。
- それを利用してカメラがどのように移動しているのかを知ることができます。
positional tracking/positional tracking/python$ python3 positional_tracking.py
![](fig/positional_tracking.png)
図に、ZED2のカメラ自体の位置の変化が表示される。

### pytorch_yolov8
object detection/custom detector/python/pytorch_yolov8$ python3 detector.py
![](fig/pytorch_yolov8.png)
- yolov8 を用いているので検出対象物の種類が増えている。
- 検出した対象物の種類はMS COCO データセットのカテゴリの番号
- ここでは検出枠の情報を用いている。

#### 注意：dockerもvenvも使わない流儀は推奨しない
- ここでは、python3 detector.py の実行時に、ultralyticsが必要になったため、 `pip3 install` している。しかし、この流儀は、ベースの環境を汚染するので好ましくない。

```
object detection/custom detector/python/pytorch_yolov8$ python detector.py
Traceback (most recent call last):
  File "detector.py", line 10, in <module>
    from ultralytics import YOLO
ModuleNotFoundError: No module named 'ultralytics'
```

--------------------------------------------------------------
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


### Q: g++ が見つからない
```
sudo apt update
sudo apt install build-essential
```

### Q: /usr/local/zed/samplesはどこ？

```
  apt update && apt install cmake -y
  cp -r /usr/local/zed/samples/depth\ sensing/ /tmp/depth-sensing
  cd /tmp/depth-sensing/cpp ; mkdir build ; cd build
  cmake .. && make
  ./ZED_Depth_Sensing
```

### Q: CUDA_TOOLKIT_ROOT_DIR
dockerを使わないで直接インストールしたら、cmakeで上記のエラーは出なかった。

### Q: Docker環境の外
Docker環境の外
$ ls /usr/local/cuda
bin                EULA.txt  lib64  README   targets
compute-sanitizer  extras    nvml   samples  tools
DOCS               include   nvvm   share    version.json

Docker環境の内
ls /usr/local/cuda
include  lib64  targets

## How about
- Docker環境の構築をやり直してはどうだろうか。
ZED SDKのインストール作業を Dockerfile中で記述してはどうだろうか？
