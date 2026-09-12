import cv2
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_dir, "input.png")
output_path = os.path.join(current_dir, "output.png")

image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.png not found!")
    exit()

gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

gx = cv2.convertScaleAbs(gx)
gy = cv2.convertScaleAbs(gy)

output = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

cv2.imwrite(output_path, output)

print("Sobel Edge Detection Completed!")