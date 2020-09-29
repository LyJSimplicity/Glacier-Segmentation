import cv2
if __name__ == "__main__":
   img = cv2.imread('Glacier.jpg')
   t,dst1 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

   # 显示图像
   cv2.imshow("origin image", img)
   cv2.imshow("THRESH_TOZERO", dst1)

   # 保存图像
   cv2.imwrite("THRESH_TOZERO.jpg", dst1)
   cv2.waitKey(0)
   cv2.destroyAllWindows()