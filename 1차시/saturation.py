import cv2
import numpy as np

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\struggling_mydei.jpg"

# 한글경로 제대로 읽기
img_array= np.fromfile(path, np.uint8)

# 이미지 읽어오기
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# 색상 회색으로 변경
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------------------------------------------------

# 50으로 채워진 더미 이미지 생성 (gray_img와 크기가 같아야 함)
# np.full 사용 또는 단순히 스칼라 값 50 사용 가능
value= 50

bright_img= cv2.add(gray_img, value)

print(f"original: {gray_img}")
print(f"after: {bright_img}")

cv2.imshow('Bright Image', bright_img)
cv2.waitKey(0)