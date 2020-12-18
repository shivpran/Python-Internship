import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (x, y, w, h) = cv2.boundingRect(cap)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite('C:/Users/Lenovo/Desktop/clouds.jpg', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
