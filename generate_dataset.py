import cv2
import os

from pathlib import Path

# Initialize the classifier
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start the video camera
vc = cv2.VideoCapture(0)

# Get the userId and userName
print("Enter the id and name of the person: ")
userId = input()
userName = input()

# Initially Count is = 1
count = 1

# Function to save the image
def saveImage(image, userName, userId, imgId):
    # Create a folder with the name as userName
    Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok=True)
    # Save the images inside the previously created folder
    cv2.imwrite("dataset/{}/{}_{}.jpg".format(userName, userId, imgId), image)
    print("[INFO] Image {} has been saved in folder : {}".format(
        imgId, userName))


print("[INFO] Video Capture is now starting please stay still...")

while True:
    # Capture the frame/image
    _, img = vc.read()

    # Copy the original Image
    originalImg = img.copy()

    # Get the gray version of our image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get the coordinates of the location of the face in the picture
    faces = faceCascade.detectMultiScale(gray_img,
                                         scaleFactor=1.2,
                                         minNeighbors=5,
                                         minSize=(50, 50))

    # Draw a rectangle at the location of the coordinates
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        coords = [x, y, w, h]

    # Show the image
    cv2.imshow("Identified Face", img)

    # Wait for user keypress
    key = cv2.waitKey(1) & 0xFF

    # Check if the pressed key is 'k' or 'q'
    if key == ord('s'):
        # If count is less than 5 then save the image
        if count <= 5:
            roi_img = originalImg[coords[1] : coords[1] + coords[3], coords[0] : coords[0] + coords[2]]
            saveImage(roi_img, userName, userId, count)
            count += 1
        else:
            break
    # If q is pressed break out of the loop
    elif key == ord('q'):
        break

print("[INFO] Dataset has been created for {}".format(userName))

# Stop the video camera
vc.release()
# Close all Windows
cv2.destroyAllWindows()
