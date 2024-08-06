import cv2
import os
import numpy as np

def prepare_training_data(data_folder_path):
    faces = []
    labels = []

    for dir_name in os.listdir(data_folder_path):
        dir_path = os.path.join(data_folder_path, dir_name)
        if not os.path.isdir(dir_path):
            print(f"Skipping {dir_path} as it is not a directory")
            continue

        try:
            label = int(dir_name)
        except ValueError:
            print(f"Skipping {dir_name} as it is not a valid label")
            continue

        print(f"Processing directory: {dir_path}")

        for filename in os.listdir(dir_path):
            if filename.lower().endswith(('.jpg', '.png')):
                image_path = os.path.join(dir_path, filename)
                image = cv2.imread(image_path)
                
                if image is None:
                    print(f"Failed to load image: {image_path}")
                    continue
                
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
                
                if len(faces_detected) == 0:
                    print(f"No faces detected in {filename}")
                
                for (x, y, w, h) in faces_detected:
                    face = gray[y:y+h, x:x+w]
                    # Resize face to a fixed size
                    face = cv2.resize(face, (200, 200))
                    faces.append(face)
                    labels.append(label)

    print(f"Number of faces: {len(faces)}")
    print(f"Number of labels: {len(labels)}")

    faces = np.array(faces)
    labels = np.array(labels, dtype=np.int32)

    return faces, labels

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

data_folder_path = 'photos'
faces, labels = prepare_training_data(data_folder_path)

if len(faces) == 0:
    print("No faces found. Training cannot be completed.")
else:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, labels)
    recognizer.save('trained_model.xml')
    print("Training complete. Model saved as 'trained_model.xml'.")
