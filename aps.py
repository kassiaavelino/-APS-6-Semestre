import cv2

aps = cv2.subtract(cv2.imread("imagem1.jpg"), cv2.imread("imagem1.jpg"))

if aps.any():
    print("são diferentes")
else:
    print("são iguais.")

