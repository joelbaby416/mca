import cv2
import math
import cvzone
from ultralytics import YOLO
import sys

# Load YOLO model with custom weights
yolo_model = YOLO("Weights/best.pt")

# Define class names
class_labels = ['With Helmet', 'Without Helmet']

# Load the image from command-line argument
if len(sys.argv) > 1:
    image_path = sys.argv[1]
    img = cv2.imread(image_path)
else:
    print("No image path provided.")
    sys.exit(1)

# Perform object detection
results = yolo_model(img)

# Loop through the detections and draw bounding boxes
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h))
        conf = math.ceil((box.conf[0] * 100)) / 100
        cls = int(box.cls[0])

        if conf > 0.1:
            cvzone.putTextRect(img, f'{class_labels[cls]} {conf}', (x1, y1 - 10), scale=0.8, thickness=1, colorR=(255, 0, 0))

# Display the image with detections
cv2.imshow("Image", img)

# Close window when 'q' button is pressed
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)