import cv2
import time
import uuid
import os

# Create data directory if it doesn't exist
DATA_DIR = './data/images'
# This will create the directory if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

labels = ['happy', 'angry', 'neutral']
number_imgs = 25

# Check if camera opens
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera could not be opened. Try a different index or check permissions.")
    exit()

for label in labels:
    print(f'Collecting images for class {label}.')
    time.sleep(3)

    # Create a folder for each label
    label_dir = os.path.join(DATA_DIR, label)
    os.makedirs(label_dir, exist_ok=True)

    for img in range(number_imgs):
        print(f'Collecting image {img+1}/{number_imgs} for {label}')

        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            continue

        # Save image in the label subfolder
        imgname = os.path.join(label_dir, f'{label}_{uuid.uuid1()}.jpg')

        # Save the image
        cv2.imwrite(imgname, frame)
        print(f"Saved: {imgname}")

        # Show image
        cv2.imshow('Capture', frame)

        # Wait and check for key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(1)

cap.release()
cv2.destroyAllWindows()
print(f"Done! Images saved to {os.path.abspath(DATA_DIR)}")
