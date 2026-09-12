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

kernel_x = np.array([[1, 0],
                     [0,-1]], dtype=np.float32)

kernel_y = np.array([[0, 1],
                     [-1,0]], dtype=np.float32)

gx = cv2.filter2D(image, -1, kernel_x)
gy = cv2.filter2D(image, -1, kernel_y)

output = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

cv2.imwrite(output_path, output)

print("Robert Edge Detection Completed!")