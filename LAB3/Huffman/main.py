import cv2
import numpy as np
import heapq
from collections import Counter


class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(data):
    frequency = Counter(data)

    heap = [Node(value, freq) for value, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]



def generate_codes(node, code="", codes={}):
    if node is None:
        return

    if node.value is not None:
        codes[node.value] = code

    generate_codes(node.left, code + "0", codes)
    generate_codes(node.right, code + "1", codes)

    return codes



def encode(data, codes):
    return "".join(codes[pixel] for pixel in data)



def decode(encoded_data, root):
    decoded = []
    current = root

    for bit in encoded_data:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.value is not None:
            decoded.append(current.value)
            current = root

    return decoded


image = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.png not found!")
    exit()

shape = image.shape
pixels = image.flatten().tolist()

root = build_tree(pixels)
codes = generate_codes(root)

encoded = encode(pixels, codes)
decoded = decode(encoded, root)

output = np.array(decoded, dtype=np.uint8).reshape(shape)

cv2.imwrite("output.png", output)

print("Huffman Coding Completed Successfully!")
print("Original Size :", len(pixels) * 8, "bits")
print("Compressed Size :", len(encoded), "bits")
print("Compression Ratio :", round((len(pixels) * 8) / len(encoded), 2))
