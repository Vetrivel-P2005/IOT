import numpy as np
import cv2
blank = 255 * np.ones((400, 400, 3), dtype="uint8")

# Line
cv2.line(blank, (50, 50), (350, 50), (255, 0, 0), 3)

# Rectangle
cv2.rectangle(blank, (50, 100), (350, 200), (0, 255, 0), 2)

# Circle
cv2.circle(blank, (200, 300), 50, (0, 0, 255), -1)  # -1 = filled

# Text
cv2.putText(blank, "Hello OpenCV!", (50, 380),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow("Shapes & Text", blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
