import cv2
import numpy as np

# Read the image
img = cv2.imread("Images/peacock.jpeg")

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Split the image into Blue, Green and Red channels
b, g, r = cv2.split(img)

# Create blank channel
zeros = np.zeros_like(b)

# Create color-separated images
red = cv2.merge([zeros, zeros, r])
green = cv2.merge([zeros, g, zeros])
blue = cv2.merge([b, zeros, zeros])

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Red Image", red)
cv2.imshow("Green Image", green)
cv2.imshow("Blue Image", blue)
cv2.imshow("Gray Image", gray)

# Save images
cv2.imwrite("Images/output_red.jpg", red)
cv2.imwrite("Images/output_green.jpg", green)
cv2.imwrite("Images/output_blue.jpg", blue)
cv2.imwrite("Images/output_gray.jpg", gray)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
