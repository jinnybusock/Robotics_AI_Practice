import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\noise_train.jpeg"

img_array= np.fromfile(path, np.uint8)
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Matplotlib 출력 위해 변환

# Gaussaian Blur 적용 (kernel size: 5x5, sigmaX= 0)
blurred_img= cv2.GaussianBlur(img, (5, 5), 0)

# Laplacian Filter 적용
laplacian_img= cv2.Laplacian(img, cv2.CV_64F)
final_img= cv2.convertScaleAbs(laplacian_img)

plt.figure(figsize= (10, 5))
plt.subplot(1,3,1), plt.imshow(img), plt.title('Original')
plt.subplot(1,3,2), plt.imshow(blurred_img), plt.title('Gaussian Blur')
plt.subplot(1,3,3), plt.imshow(final_img), plt.title('Laplacian Image')
plt.show()