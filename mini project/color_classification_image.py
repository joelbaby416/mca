import cv2
import argparse
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os
import os.path
from pathlib import Path
import time

# Initialize global variables
prediction = 'n.a.'
clicked_x, clicked_y = -1, -1  # Store click position
prediction_time = 0  # Store the time when a prediction is made


# Mouse callback function to get click position and detect color
def click_event(event, x, y, flags, param):
    global clicked_x, clicked_y, prediction, prediction_time, source_image

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_x, clicked_y = x, y
        
        # Reload the original image to clear previous predictions
        source_image = cv2.imread(image_path)

        # Crop a small area around the clicked point
        clicked_region = source_image[max(0, y-5):y+5, max(0, x-5):x+5]

        # Predict the color of the clicked region
        color_histogram_feature_extraction.color_histogram_of_test_image(clicked_region)
        prediction = knn_classifier.main('training.data', 'test.data')

        # Record the time of the prediction
        prediction_time = time.time()

        # Get image dimensions to adjust text position
        img_height, img_width = source_image.shape[:2]

        # Calculate the position for text relative to the click
        if x > img_width // 2:  # If click is on the right half, text goes to the left
            text_x = x - 200  # Move the text left by 200 pixels
        else:  # If click is on the left half, text goes to the right
            text_x = x + 20  # Move the text right by 20 pixels

        # Ensure text doesn't go out of image boundaries
        text_x = max(0, min(text_x, img_width - 200))
        text_y = max(30, y)  # Set text above the clicked point

        # Display the predicted color at the calculated location
        cv2.putText(source_image, f'Prediction: {prediction}', (text_x, text_y), 
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow('Color Classifier', source_image)


# Argument parser for the command-line inputs
parser = argparse.ArgumentParser(description="Color Classification from Image")
parser.add_argument('-i', '--image', required=True, help='Path to the image file')
args = parser.parse_args()

# Load the test image using the provided argument
image_path = args.image
source_image = cv2.imread(image_path)
if source_image is None:
    print(f"Error: Cannot load image at path {image_path}")
    exit(1)

# Path to the training data
PATH = Path('./training.data')

# Checking whether the training data is ready
if PATH.is_file() and os.access(PATH, os.R_OK):
    print('Training data is ready, classifier is loading...')
else:
    print('Training data is being created...')
    with open(PATH, 'w'):
        pass
    color_histogram_feature_extraction.training()
    print('Training data is ready, classifier is loading...')

# Set up the mouse callback function to capture click events
cv2.imshow('Color Classifier', source_image)
cv2.setMouseCallback('Color Classifier', click_event)

# Wait for the user to press 'q' to quit
while True:
    # If a prediction has been made, check if 5 seconds have passed
    if prediction != 'n.a.' and (time.time() - prediction_time) > 5:
        # Remove the prediction text after 5 seconds by reloading the original image
        prediction = 'n.a.'
        source_image = cv2.imread(image_path)
    
    # Display the image
    cv2.imshow('Color Classifier', source_image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
