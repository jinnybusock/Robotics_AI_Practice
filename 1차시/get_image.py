import cv2
import numpy as np

path= r"C:\Users\jinny\Desktop\두산로보틱스 부트캠프\AI\AI 개론 응용\image\struggling_mydei.jpg"

# 한글경로 제대로 읽기
img_array= np.fromfile(path, np.uint8)

# 이미지 읽어오기
img= cv2.imdecode(img_array, cv2.IMREAD_COLOR)

if img is None:
    print("이미지를 찾을 수 없습니다.")

else:
    # 이미지 형태 출력
    print("Shape: ", img.shape)
    print(f"차원: {img.ndim}")
    print(f"데이터 타입:{img.dtype}")