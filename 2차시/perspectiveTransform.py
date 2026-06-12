import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\perspective_image.jpg"

img_array= np.fromfile(path, np.uint8)
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Matplotlib 출력 위해 변환

# ---------------------------------------

# 찌그러진 문서 정면에서 본 것처럼 펼치기
h, w= img.shape[:2]

# 좌표- 시계방향(좌상 --> 우상 --> 우하 --> 좌하)
img_pts= np.array([[0.0, 0.0], [w, 0.0], [w, h], [0.0, h]], dtype= np.float32)
after_pts= np.array([[0.0, 0.0], [w+ 20, 0.0], [w+20, h], [0.0, h]], dtype= np.float32)

# 변환 행렬 계산
matrix= cv2.getPerspectiveTransform(img_pts, after_pts)

# 원근 변환 적용
# cv2.warpPerspective(src, matrix, (w, h))
#   - w, h: 원하는 사이즈
#   - borderValue(BGR) 빈 공간 색상
after_img= cv2.warpPerspective(img, matrix, (w, h), borderValue= (0, 255, 255))

plt.imshow(after_img)
plt.show()