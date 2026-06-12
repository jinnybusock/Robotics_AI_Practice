import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\noise_train.jpeg"

img_array= np.fromfile(path, np.uint8)
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Matplotlib 출력 위해 변환

h,w= img.shape[:2]

# ---------------------------------------

# 가로, 세로 모두 0.5배로 축소
# dsize를 (0,0)으로 두고 fx, fy 활용
resized_img= cv2.resize(img, dsize= (0,0), fx= 0.5, fy= 0.5, interpolation= cv2.INTER_NEAREST)

print(f"Original shape: {img.shape}")
print(f"Resized Shape: {resized_img.shape}")