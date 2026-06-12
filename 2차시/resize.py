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

after_h= h//2
after_w= w//2

# dsize= destination size
# interpolatoin: 보간 방법
resized_img= cv2.resize(img, dsize= (after_w, after_h), interpolation= cv2.INTER_NEAREST)

plt.subplot(1,2,1), plt.imshow(img)
plt.subplot(1,2,2), plt.imshow(resized_img)
plt.show()