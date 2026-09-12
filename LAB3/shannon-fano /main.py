import cv2
import numpy as np
from collections import Counter
import os


# ---------------- Shannon-Fano Functions ---------------- #
def build_codes(symbols, codes={}, prefix=""):
    if len(symbols) == 1:
        codes[symbols[0][0]] = prefix if prefix else "0"
        return

    total = sum(freq for _, freq in symbols)
    acc = 0
    split = 0

    for i, (_, freq) in enumerate(symbols):
        acc += freq
        if acc >= total / 2:
            split = i
            break

    left = symbols[:split + 1]
    right = symbols[split + 1:]

    build_codes(left, codes, prefix + "0")

    if right:
        build_codes(right, codes, prefix + "1")

    return codes


# ---------------- Main ---------------- #
current_dir = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(current_dir, "input.png")
output_path = os.path.join(current_dir, "output.png")

image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.png not found!")
    exit()

shape = image.shape
pixels = image.flatten().tolist()

frequency = Counter(pixels)
symbols = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

codes = build_codes(symbols)

# Encode
encoded = "".join(codes[p] for p in pixels)

# Reverse dictionary
reverse_codes = {v: k for k, v in codes.items()}

# Decode
decoded = []
temp = ""

for bit in encoded:
    temp += bit
    if temp in reverse_codes:
        decoded.append(reverse_codes[temp])
        temp = ""

decoded = np.array(decoded, dtype=np.uint8).reshape(shape)

cv2.imwrite(output_path, decoded)

print("Shannon-Fano Coding Completed Successfully!")
print("Original Size :", len(pixels) * 8, "bits")
print("Compressed Size :", len(encoded), "bits")
print("Compression Ratio :", round((len(pixels) * 8) / len(encoded), 2))