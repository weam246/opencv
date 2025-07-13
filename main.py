import cv2
import numpy as np

# Load image
image = cv2.imread('image.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color ranges in HSV
colors = {
    "Red": [(0, 120, 70), (10, 255, 255)],
    "Green": [(40, 40, 40), (80, 255, 255)],
    "Yellow": [(20, 100, 100), (30, 255, 255)]
}

for color, (lower, upper) in colors.items():
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(image, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

cv2.imshow("Color Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
