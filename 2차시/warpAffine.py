import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\noise_train.jpeg"

img_array= np.fromfile(path, np.uint8)
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Matplotlib 출력 위해 변환

# ---------------------------------------

# 중심점을 기준으로 반시계 방향으로 45도 회전

# img.shape= [h, w, c]
h,w= img.shape[:2]
# 이미지 중심점
center= (w//2, h//2)

angle= 45
scale= 1.0
# 기하학적 변환: 이미지 * 행렬 결과물
# getRotationMatrix2D: 원본에 곱할 행렬 만들기
matrix= cv2.getRotationMatrix2D(center, angle, scale)

# warpAffine(원본 이미지, 곱할 행렬, (너비, 높이))
rotated_img= cv2.warpAffine(img, matrix, (w, h))

plt.imshow(rotated_img)
plt.title('Rotated Image')
plt.show()