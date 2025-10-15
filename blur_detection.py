# blur_detection.py
import cv2

def is_blurry(image_path, threshold=100):
    """
    使用拉普拉斯方差法判断图像是否模糊
    :param image_path: 图像路径
    :param threshold: 阈值，低于此值认为是模糊（可根据实际情况调整）
    :return: 清晰度分数 和 是否模糊
    """
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("❌ 错误：无法加载图片，请检查路径和文件名")
        return None, None

    # 转为灰度图（边缘信息更明显）
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 计算拉普拉斯算子的方差
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # 判断是否模糊
    is_blur = laplacian_var < threshold
    result = "清晰" if not is_blur else "模糊"

    print(f"📸 {image_path}")
    print(f"🔍 清晰度得分: {laplacian_var:.2f}")
    print(f"📌 判定结果: {result} {'⚠️' if is_blur else '✅'}")

    return laplacian_var, is_blur


# === 主程序入口 ===
if __name__ == "__main__":
    # 测试两张图（请提前准备好）
    is_blurry("clear.jpg", threshold=100)
    is_blurry("blurred.jpg", threshold=100)