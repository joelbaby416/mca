// Handle form submission for file upload
document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault();

    // Simulate color detection result
    const detectedColor = "#3498db"; // Example color (replace with actual color detection logic)

    // Update result section
    document.getElementById("colorName").innerText = "Color Name: Blue"; // Example name
    document.getElementById("colorBox").style.backgroundColor = detectedColor;
});

// Handle live feed button click to access the webcam
const liveFeedLabel = document.getElementById('liveFeedLabel');
const video = document.getElementById('webcamFeed');

function startWebcam() {
    // Check if the browser supports getUserMedia
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            // Display the video feed
            video.style.display = 'block';
            video.srcObject = stream;
        })
        .catch(function(error) {
            console.log("Error accessing webcam: " + error);
        });
    } else {
        alert("Your browser does not support webcam access.");
    }
}

// Trigger webcam feed when live feed label is clicked
liveFeedLabel.addEventListener('click', startWebcam);
