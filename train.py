import cv2
import pandas as pd
from datetime import datetime

# Define a mapping of labels to actual names
label_to_name = {
    1: "Allmin",  # Update with actual names/IDs
    2: "AnotherName",
    # Add more mappings as needed
}

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_model.xml')

# Load the face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the video capture
video_capture = cv2.VideoCapture(0)  # 0 is the default camera

# Initialize the list to store data
data = []

# Define a threshold for confidence to consider a face as detected
confidence_threshold = 70.0

# Create a resizable window
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Check if the frame was captured correctly
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    face_detected_flag = False

    # Process each detected face
    for (x, y, w, h) in faces_detected:
        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)
        name = label_to_name.get(label, "Unknown")  # Get name from the mapping or default to "Unknown"
        label_text = f"Name: {name}, Label: {label}, Confidence: {confidence:.2f}"

        # Draw a rectangle around the face and add label text
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Add some padding for text
        text_position = (x, y - 10 if y - 10 > 10 else y + h + 20)  # Adjust to be within frame

        # Adjust font size and position if needed
        cv2.putText(frame, label_text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        # Check if the detected label and confidence exceed the threshold
        if confidence < confidence_threshold:
            face_detected_flag = True
            # Add the data to the list with the current timestamp
            data.append({
                'Name': name,
                'Label': label,
                'Confidence': confidence,
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

    # Display "Present" on the frame if a face is detected
    if face_detected_flag:
        cv2.putText(frame, "Present", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Save data to Excel with date and time
try:
    df = pd.DataFrame(data)
    df.to_excel('face_data_with_names_and_time.xlsx', index=False)
    print("Data saved to 'face_data_with_names_and_time.xlsx'")
except PermissionError as e:
    print(f"Error saving data to Excel: {e}")
