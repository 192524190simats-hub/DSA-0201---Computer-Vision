import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Open file dialog to select an image
Tk().withdraw()
file_path = askopenfilename(title="Select an Image")

# Read the image
image = cv2.imread(file_path)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges using Canny
edges = cv2.Canny(gray, 100, 200)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
