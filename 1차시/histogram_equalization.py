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

equalized_img= cv2.equalizeHist(gray_img)
cv2.imshow("Result", equalized_img)
cv2.imshow("Original Gray Pic", gray_img)
cv2.waitKey(0)