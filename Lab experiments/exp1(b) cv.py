import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Open file dialog to select an image
Tk().withdraw()
file_path = askopenfilename(title="Select an Image")

# Read the image
image = cv2.imread(file_path)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(image, (5, 5), 0)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
