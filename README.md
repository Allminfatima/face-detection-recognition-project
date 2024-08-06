# face-detection-recognition-project

## Description
This project demonstrates a real-time face recognition system built using Python and OpenCV. The system trains a face recognizer model with labeled images, performs real-time face detection and recognition via webcam, and saves the recognized face data along with confidence scores and timestamps into an Excel file. The project also handles error scenarios and adjusts the camera UI for better visibility.
It consists of three Python scripts and one folder containing images. The setup includes training a face recognition model and using it for detecting faces in real-time, with results logged to an Excel file.

## Features
- Train face recognizer model with images.
- Real-time face detection and recognition using webcam.
- Save recognized face data, confidence scores, and timestamps to an Excel file.
- Dynamic camera UI adjustments.
- Error handling and data visualization.

## Files and Folder

1. **`train_face_recognizer.py`**
   - **Description:** This script trains a face recognition model using images provided in the `photos` folder. It reads images from subdirectories, prepares training data, and saves the model to an XML file.
   
2. **`train.py`**
   - **Description:** This script performs real-time face recognition using the trained model. It opens a camera feed, detects faces, annotates them with names and confidence scores, and saves recognition data to an Excel file.

3. **`trained_model.xml`**
   - **Description:** This XML file contains the trained face recognition model. It starts as an empty file but gets populated with data when you run `train_face_recognizer.py`.

4. **`photos/`**
   - **Description:** This folder contains images used for training the face recognition model. It has two subfolders:
     -  Contains images for one person (e.g., `Allmin.jpg`, `pic.jpg`).
     -  Contains images for another person (e.g., `xyz.jpg`, `pic2.jpg`).
   - **Note:** You can add more images to these subfolders as needed. Multiple subfolders are used to separate images for different people for better training accuracy.

## Instructions

1. **Setup Dependencies:**
   - Ensure all required packages are installed. Create a virtual environment and install dependencies from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt


2. **Prepare Training Data:**
   - Run train_face_recognizer.py to train the model using images in the photos folder.
   ```bash
   python train_face_recognizer.py

-> This will generate and save the trained_model.xml file with the trained data.


3. **Run Face Recognition:**
   - Execute train.py to start the real-time face recognition process.
   ```bash
   python train.py
   
-> The script will:
- Open the camera feed.
- Detect faces and recognize them.
- Display the recognized face labels and confidence scores on the camera feed.
- Save the recognition data (name, confidence, date, and time) to an Excel file named face_data_with_names_and_time.xlsx in the same directory.

4. **Results:**
   - **1**: The recognition data will be automatically saved to face_data_with_names_and_time.xlsx.
   - **2**: The camera feed will show real-time face detection results with annotations.


5. **Output Examples:**
   
   **a**. Excel File Example:**
   
   | Name   | Confidence | Date                | Time   |
   |--------|------------|---------------------|--------|
   | Allmin | 75.91      | 2024-08-06          | 12:34:56|

   **b**: Camera Feed Example:**
    ![Screenshot 2024-08-06 122256](https://github.com/user-attachments/assets/3777bdec-272e-4b0c-b703-c5c8c6b7a18c)

   **Note:** To close the camera feed, press the `q` key.

   **c**: Terminal Output Example:**

    ![Screenshot 2024-08-06 122344](https://github.com/user-attachments/assets/e73d5874-e4bf-450e-840c-860e24ca0898)



7. **Notes**
    - Ensure your camera is properly connected and accessible by OpenCV.
    - The requirements.txt file should contain all necessary dependencies. If you encounter issues, check that all packages listed are correctly installed.
    - Modify and add images in the photos folder as needed for training more faces.

     
## Setup
**Clone the Repository:**
   ```bash
   git clone https://github.com/Allminfatima/face-detection-recognition-project.git
