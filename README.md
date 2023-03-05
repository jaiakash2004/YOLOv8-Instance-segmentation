# YOLOv8-Instance-segmentation
This repository contains YOLOv8 Instance segmantation detection in python using trained and pre-trained models. 

Documentation
See below for a quickstart installation and usage example, and see the YOLOv8 Docs for full documentation on training, validation, prediction and deployment.

Install
Pip install the ultralytics package including all requirements.txt in a Python>=3.7 environment with PyTorch>=1.7.

pip install ultralytics
Usage
CLI
YOLOv8 may be used directly in the Command Line Interface (CLI) with a yolo command:

yolo predict model=yolov8n.pt source="https://ultralytics.com/images/bus.jpg"
yolo can be used for a variety of tasks and modes and accepts additional arguments, i.e. imgsz=640. See the YOLOv8 CLI Docs for examples.

Python
YOLOv8 may also be used directly in a Python environment, and accepts the same arguments as in the CLI example above:

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco128.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
success = model.export(format="onnx")  # export the model to ONNX format
Models download automatically from the latest Ultralytics release. See YOLOv8 Python Docs for more examples.

Model Architectures
⭐ NEW YOLOv5u anchor free models are now available.

All supported model architectures can be found in the Models section.

Known Issues / TODOs
We are still working on several parts of YOLOv8! We aim to have these completed soon to bring the YOLOv8 feature set up to par with YOLOv5, including export and inference to all the same formats. We are also writing a YOLOv8 paper which we will submit to arxiv.org once complete.

 TensorFlow exports
 DDP resume
 arxiv.org paper
Models
All YOLOv8 pretrained models are available here. Detection and Segmentation models are pretrained on the COCO dataset, while Classification models are pretrained on the ImageNet dataset.

Models download automatically from the latest Ultralytics release on first use.
