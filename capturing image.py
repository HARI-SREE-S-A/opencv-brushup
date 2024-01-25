import cv2

cap = cv2.VideoCapture(0)

while True:
    success,img = cap.read()

    cv2.imshow("kive", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
