import cv2
import numpy as np
if __name__ == "__main__":
   img = cv2.imread('Glacier.jpg')
   img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#原图像不是灰度图，必须先转换为灰度图
   #普通二值化阈值处理
   t1, dst1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
   #自适应阈值处理，采用均值计算阈值
   dst2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)
   #自适应阈值处理，采用高斯均值计算阈值
   dst3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)

   # 创建窗口
   cv2.namedWindow("origin image",cv2.WINDOW_NORMAL)#cv2.WINDOW_NORMAL使窗口大小可调整
   cv2.namedWindow("THRESH_BINARY",cv2.WINDOW_NORMAL)
   cv2.namedWindow("MEAN_C",cv2.WINDOW_NORMAL)
   cv2.namedWindow("GAUSSIAN_C", cv2.WINDOW_NORMAL)
   # 显示图像
   cv2.imshow("origin image", img)
   cv2.imshow("THRESH_BINARY", dst1)
   cv2.imshow("MEAN_C",dst2)
   cv2.imshow("GAUSSIAN_C", dst3)

   # 保存图像
   cv2.imwrite("THRESH_BINARY7.jpg", dst1)
   cv2.imwrite("MEAN_C7.jpg", dst2)
   cv2.imwrite("GAUSSIAN_C7.jpg", dst3)
   cv2.waitKey(0)
   cv2.destroyAllWindows()