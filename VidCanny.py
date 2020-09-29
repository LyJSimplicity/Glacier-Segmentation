import cv2

def video_canny(video):
    cap = cv2.VideoCapture(video)
    while 1:
        ret,frame = cap.read()
        img = frame
        if ret:
            img_resize = cv2.resize(img,(1080,607))
            blurred = cv2.GaussianBlur(img_resize, (3, 3), 0)
            gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
            xgrad = cv2.Sobel(gray, cv2.CV_16SC1, 1, 0)
            ygrad = cv2.Sobel(gray, cv2.CV_16SC1, 0, 1)
            output = cv2.Canny(xgrad, ygrad, 50, 150)
            cv2.imshow("Video", output)

            if cv2.waitKey(24)  &  0xFF==27:
                break

        else:
            break

            cap.release()
            cv2.destroyAllWindows()

video_canny("YourName.mp4")


