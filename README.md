<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ADMP/blob/master/example/pulseai_logo.png'>
</div>

<h1 align="center">
    Automatic Detection System of Parcels Based on Deep Learning Algorithms
</h1>

---
<p align="center">
    <em>ADMP is an automatic model for parcels detection which based on deep learning algorithms.</em>
    <br>
        <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License"> 
    </a>
    <a href="https://github.com/pyecharts/pyecharts/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://pypi.org/project/pyecharts/">
        <img src="https://img.shields.io/badge/python-3.x-blue.svg" >
    </a>
</p>

## Introduction
---
As the key work of logistics and security industry, the detection of package carriers undertakes the important task of preventing dangerous contraband from entering the transport channels. Tight time, heavy tasks and less personnel，which has always been a difficult problem in front of security inspection. With the continuous development of passenger logistics industry, the huge number of parcels has far exceeded the scope of manual processing, which has brought great challenges to the logistics industry and security industry. In recent years, the breakthrough of deep learning technology has made high-precision target detection technology widely used and achieved remarkable achievements, which makes it possible to apply target detection technology to security inspection work.Based on three target detection algorithms, this paper establishes models to learn 1406 image data containing five types of contraband, after training for 100,000 times, the optimal mAP was stable at about 83.62%. Using several X-Ray images to be tested, the detection model successfully detects the prohibited items in the image. At last, the deployment mode of "combination of the end and cloud" is proposed for model deployment, and the suggestions of the practical application and improvement direction of the detection model are proposed.

<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training_model/example/1.png'>
</div>

----
# Front-end based on Flask and echarts
In order to use the model more conveniently, I designed a simple front-end based on Flask and echarts, and it looks great！
<div align='center'>
    <img src= 'https://github.com/Mingqi-Yuan/ADMP/blob/master/file_for_training_model/example.png'>
</div>
---
# Get it now
Clone it：
```
$ git clone https://github.com/Mingqi-Yuan/ADMP.git
```
or  you can get the zip file，then make a new **Flask project** with **PyCharm**.
```
$  wget https://codeload.github.com/Mingqi-Yuan/ADMP/zip/master
```



---
# Package required
The moudle below is required for the ADMP:
|Name|
|--|
| TensorFlow、TensorFlow Object Detection API |
| Flask|
| json | 
| NumPy|
|OpenCV|
|PIL|
The python environment of **Anaconda3** is recommended.Hope you will have fun with it!

---

# License
[MIT License](LICENSE)
