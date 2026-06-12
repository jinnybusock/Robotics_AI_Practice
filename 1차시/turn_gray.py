import cv2
import numpy as np

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\struggling_mydei.jpg"

# 한글경로 제대로 읽기
img_array= np.fromfile(path, np.uint8)

# 이미지 읽어오기
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# -------------------------------------------------

# 색상 회색으로 변경
gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 원본 이미지 B, G, R 채널로 분리
b, g, r= cv2.split(img)

print(f"Grayscale shape: {gray_img.shape}")
print(f"Blue channel: {b.shape}")
print(f"Green channel: {g.shape}")
print(f"Red channel: {r.shape}")

# 이미지 띄우기 (창 제목, 띄울 이미지 변수)
cv2.imshow('Original image', img)
cv2.imshow('Grayscale Image', gray_img)
cv2.imshow('Red channel', r)

# 키보드 입력이 올 때까지 화면 끄지 않고 무한 대기
cv2.waitKey(0)

# 아무 키나 누르면 열려 있던 모든 이미지 창 닫기
cv2.destroyAllWindows()