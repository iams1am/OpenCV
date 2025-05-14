Creat OpenCV environment in VS Code

Microsoft Windows [Version 10.0.22631.4890]
(c) Microsoft Corporation. All rights reserved.
#Change to CMD from powershell

E:\OpenCV>python -m venv myenv

E:\OpenCV>myenv\Scripts\activate

(myenv) E:\OpenCV>pip install opencv-python
Collecting opencv-python
  Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.whl.metadata (20 kB)
Collecting numpy>=1.21.2 (from opencv-python)
  Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl.metadata (60 kB)
data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.whl (39.5 MB)
Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl (12.6 data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.data (60 kB)
data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.data (60 kB)
data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.data (60 kB)
data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.whl (39.5 MB)
data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.whl (39.5 MB)
Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl (12.6 data (60 kB)
Using cached opencv_python-4.11.0.86-cp37-abi3-win_amd64.whl (39.5 MB)
whl (39.5 MB)
Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl (12.6 MB)
Using cached numpy-2.2.3-cp313-cp313-win_amd64.whl (12.6 MB)
MB)
Installing collected packages: numpy, opencv-python      
Successfully installed numpy-2.2.3 opencv-python-4.11.0.86
Successfully installed numpy-2.2.3 opencv-python-4.11.0.8Successfully installed numpy-2.2.3 opencv-python-4.11.0.8Successfully installed numpy-2.2.3 opencv-python-4.11.0.8Successfully installed numpy-2.2.3 opencv-python-4.11.0.8Successfully installed numpy-2.2.3 opencv-python-4.11.0.86

[notice] A new release of pip is available: 24.3.1 -> 25.0.1


(myenv) E:\OpenCV>pip install matplotlib
Collecting matplotlib
  Downloading matplotlib-3.10.1-cp313-cp313-win_amd64.whl.metadata (11 kB)
Collecting contourpy>=1.0.1 (from matplotlib)
  Downloading contourpy-1.3.1-cp313-cp313-win_amd64.whl.metadata (5.4 kB)
Collecting cycler>=0.10 (from matplotlib)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib)
  Downloading fonttools-4.56.0-cp313-cp313-win_amd64.whl.metadata (103 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib)
  Downloading kiwisolver-1.4.8-cp313-cp313-win_amd64.whl.metadata (6.3 kB)
Requirement already satisfied: numpy>=1.23 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (2.2.3)
Collecting packaging>=20.0 (from matplotlib)
  Downloading packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
Collecting pillow>=8 (from matplotlib)
  Downloading pillow-11.1.0-cp313-cp313-win_amd64.whl.metadata (9.3 kB)
Collecting pyparsing>=2.3.1 (from matplotlib)
  Downloading pyparsing-3.2.1-py3-none-any.whl.metadata (5.0 kB)
Collecting python-dateutil>=2.7 (from matplotlib)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting six>=1.5 (from python-dateutil>=2.7->matplotlib)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading matplotlib-3.10.1-cp313-cp313-win_amd64.whl (8.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.1/8.1 MB 68.9 kB/s eta 0:00:00    
Downloading contourpy-1.3.1-cp313-cp313-win_amd64.whl (220 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.56.0-cp313-cp313-win_amd64.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 115.0 kB/s eta 0:00:00   
Downloading kiwisolver-1.4.8-cp313-cp313-win_amd64.whl (71 kB)
Downloading packaging-24.2-py3-none-any.whl (65 kB)
Downloading pillow-11.1.0-cp313-cp313-win_amd64.whl (2.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 MB 87.5 kB/s eta 0:00:00    
Downloading pyparsing-3.2.1-py3-none-any.whl (107 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, pillow, packaging, kiwisolver, fonttools, cycler, contourpy, python-dateutil, matplotlib
Successfully installed contourpy-1.3.1 cycler-0.12.1 fonttools-4.56.0 kiwisolver-1.4.8 matplotlib-3.10.1 packaging-24.2 pillow-11.1.0 pyparsing-3.2.1 python-dateutil-2.9.0.post0 six-1.17.0

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(myenv) E:\OpenCV>pip install numpy
Requirement already satisfied: numpy in e:\opencv\myenv\lib\site-packages (2.2.3)

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(myenv) E:\OpenCV>pip install opencv-python matplotlib numpy
Requirement already satisfied: opencv-python in e:\duburi_opencv\myenv\lib\site-packages (4.11.0.86)
Requirement already satisfied: matplotlib in e:\duburi_opencv\myenv\lib\site-packages (3.10.1)
Requirement already satisfied: numpy in e:\duburi_opencv\myenv\lib\site-packages (2.2.3)
Requirement already satisfied: contourpy>=1.0.1 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (1.3.1)
Requirement already satisfied: cycler>=0.10 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (4.56.0)
Requirement already satisfied: kiwisolver>=1.3.1 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (1.4.8)
Requirement already satisfied: packaging>=20.0 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (24.2)
Requirement already satisfied: pillow>=8 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (11.1.0)
Requirement already satisfied: pyparsing>=2.3.1 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (3.2.1)
Requirement already satisfied: python-dateutil>=2.7 in e:\duburi_opencv\myenv\lib\site-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in e:\duburi_opencv\myenv\lib\site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(myenv) E:\OpenCV>python duburi_test.py
Processing 1/5: blue_yellow_gradient.jpg
Grayscale image saved to sample_grayscale\gray_blue_yellow_gradient.jpg
Processing 2/5: checkerboard.jpg
Grayscale image saved to sample_grayscale\gray_checkerboard.jpg
Processing 3/5: concentric_circles.jpg
Grayscale image saved to sample_grayscale\gray_concentric_circles.jpg
Processing 4/5: rainbow_pattern.jpg
Grayscale image saved to sample_grayscale\gray_rainbow_pattern.jpg
Processing 5/5: red_green_gradient.jpg
Grayscale image saved to sample_grayscale\gray_red_green_gradient.jpg
