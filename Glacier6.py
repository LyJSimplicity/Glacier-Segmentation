import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread('Glacier.jpg')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 原图像不是灰度图，必须先转换为灰度图
    # 普通二值化阈值处理
    t1, dst1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # 采用OTSU的处理
    t2, dst2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 创建窗口
    cv2.namedWindow("origin image", cv2.WINDOW_NORMAL)  # cv2.WINDOW_NORMAL使窗口大小可调整
    cv2.namedWindow("THRESH_TOZERO", cv2.WINDOW_NORMAL)
    cv2.namedWindow("THRESH_OTSU", cv2.WINDOW_NORMAL)
    # 显示图像
    cv2.imshow("origin image", img)
    cv2.imshow("THRESH_TOZERO", dst1)
    cv2.imshow("THRESH_OTSU", dst2)

    # 保存图像
    cv2.imwrite("THRESH_TOZERO6.jpg", dst1)
    cv2.imwrite("THRESH_OTSU6.jpg", dst2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()