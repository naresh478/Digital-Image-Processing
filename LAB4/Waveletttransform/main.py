import cv2
import numpy as np
import pywt
import os

# Current folder
current_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_dir, "input.png")
output_path = os.path.join(current_dir, "output.png")

# Read image in grayscale
image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.png not found!")
    exit()

# Haar Wavelet Transform
LL, (LH, HL, HH) = pywt.dwt2(image, 'haar')

# Normalize each component for display
LL = cv2.normalize(LL, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
LH = cv2.normalize(np.abs(LH), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
HL = cv2.normalize(np.abs(HL), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
HH = cv2.normalize(np.abs(HH), None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Combine into one output image
top = np.hstack((LL, LH))
bottom = np.hstack((HL, HH))
output = np.vstack((top, bottom))

# Save output
cv2.imwrite(output_path, output)

print("Wavelet Transform Completed Successfully!")
print("Output saved as output.png")