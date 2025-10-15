# generate_test_images.py
import numpy as np
import cv2

# 创建一张清晰的测试图（黑白条纹 + 文字）
img = np.zeros((400, 600), dtype=np.uint8)

# 画竖条纹
for i in range(0, 600, 20):
    cv2.rectangle(img, (i, 0), (i+10, 400), 255, -1)

# 添加文字和矩形
cv2.putText(img, "Test Image", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, 0, 3)
cv2.rectangle(img, (100, 150), (300, 300), 128, 3)

# 保存清晰图
cv2.imwrite("clear.jpg", img)
print("✅ 已生成 clear.jpg")

# 生成模糊图
blurred = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite("blurred.jpg", blurred)
print("✅ 已生成 blurred.jpg")
