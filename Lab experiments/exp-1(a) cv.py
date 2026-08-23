import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # Hide the Tkinter window

file_path = askopenfilename(title="Select an Image")

image = cv2.imread(file_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
