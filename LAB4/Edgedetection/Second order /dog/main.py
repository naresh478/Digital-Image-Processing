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

blur1 = cv2.GaussianBlur(image, (5,5), 1)
blur2 = cv2.GaussianBlur(image, (9,9), 2)

dog = cv2.absdiff(blur1, blur2)

cv2.imwrite(output_path, dog)

print("Difference of Gaussian Completed!")