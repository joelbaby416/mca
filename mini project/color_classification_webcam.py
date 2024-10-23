import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera
ret, frame = cap.read()
prediction = 'n.a.'

# Path to training data
PATH = './training.data'

# Check if the training data is available
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print('Training data is ready, classifier is loading...')
else:
    print('Training data is being created...')
    with open('training.data', 'w') as f:
        pass
    color_histogram_feature_extraction.training()
    print('Training data is ready, classifier is loading...')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Display the prediction on the frame
    cv2.putText(
        frame,
        f'Prediction: {prediction}',
        (15, 45),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (200, 200, 200),
        2
    )

    # Display the frame
    cv2.imshow('Color Classifier', frame)

    # Extract color histogram and predict
    color_histogram_feature_extraction.color_histogram_of_test_image(frame)
    prediction = knn_classifier.main('training.data', 'test.data')

    # Exit the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
