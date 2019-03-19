# ADMP
Automatic Detection Model of Parcels Based on Deep Learning Algorithms

Training with Tesla P40

Here are the training data:

![1](https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training/example/1.png)

![2](https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training/example/2.png)

![3](https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training/example/loss.png)

![4](https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training/example/mAP.png)

![5](https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training/example/AR.png)

---

1. The environment：

- Python 3.6
- TensorFlow 1.9
- TensorFlow Object Detection API
- Keras 2.1.5
- CUDA 9.0
- CuDnn 7.1

2. The dataset：

Use **csv_to_tfrecords.py** to generate the TFRecords

3. Training：

Use **the model_main.py** to train the model

4. Export:

Use the **export_inference_graph.py** to export the frozen model

5. Detection:

Use the **detect.py** to detect new images with frozen model

6. About the YOLO V3

Please refer to the [keras-yolov3](https://github.com/qqwweee/keras-yolo3)
