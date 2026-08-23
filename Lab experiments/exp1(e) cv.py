import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Open file dialog to select an image
Tk().withdraw()
file_path = askopenfilename(title="Select an Image")

# Read the image
image = cv2.imread(file_path)

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Erode the image
eroded = cv2.erode(image, kernel, iterations=1)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
