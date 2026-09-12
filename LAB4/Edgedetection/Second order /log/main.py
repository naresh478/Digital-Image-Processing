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

blur = cv2.GaussianBlur(image, (3,3), 0)
log = cv2.Laplacian(blur, cv2.CV_64F)

output = cv2.convertScaleAbs(log)

cv2.imwrite(output_path, output)

print("Laplacian of Gaussian Completed!")