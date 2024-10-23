import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from knn_classifier import main  # type: ignore # Assuming knn_classifier.main() is your KNN prediction function

# Load dataset (replace with actual loading method)
data = np.array([
    # Add your actual data here
    (139, 0, 0, 'red'), (204, 22, 0, 'red'), (206, 0, 25, 'red'),
    (220, 0, 3, 'red'), (254, 0, 0, 'red'), # ... more data ...
    (0, 0, 254, 'blue'), (0, 0, 255, 'blue'), (1, 119, 193, 'blue')
])

# Extract features and labels
X = data[:, :-1].astype(float)  # RGB values
y = data[:, -1]  # Color labels

# Encode labels to integers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Save the training data (necessary for KNN classifier)
np.savetxt('training_split.data', np.column_stack((X_train, y_train)), delimiter=',')

# Variables to keep track of predictions
correct_predictions = 0
total_predictions = len(X_test)

# Loop through the test set and make predictions
for i in range(total_predictions):
    # Create a temporary file for the test data
    np.savetxt('test_instance.data', X_test[i].reshape(1, -1), delimiter=',')

    # Predict using KNN
    prediction = main('training_split.data', 'test_instance.data')

    # Debug: Print the raw prediction value
    print(f"Raw prediction: {prediction}")

    # Convert the predicted label (which may be a float) to an integer safely
    try:
        predicted_index = int(float(prediction))  # Safely convert the prediction to an integer
    except ValueError as e:
        print(f"Error converting prediction: {e}")
        continue

    # Convert the predicted index back to a string label using the label encoder
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]

    # Compare prediction to actual label
    actual_label = label_encoder.inverse_transform([y_test[i]])[0]
    
    if predicted_label == actual_label:
        correct_predictions += 1
    else:
        print(f"Prediction mismatch: predicted {predicted_label}, actual {actual_label}")

# Print final accuracy
accuracy = correct_predictions / total_predictions * 100
print(f"Accuracy: {accuracy}%")
