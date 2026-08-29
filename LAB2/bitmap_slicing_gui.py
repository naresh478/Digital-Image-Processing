import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt

# Global variables
image_path = None
saved_bit_planes = []


def upload_image():
    global image_path

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp *.tif *.tiff"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        image_path = file_path

        img = Image.open(file_path)
        img.thumbnail((300, 300))

        photo = ImageTk.PhotoImage(img)

        image_label.config(image=photo)
        image_label.image = photo


def bit_plane_slicing():

    global saved_bit_planes

    if image_path is None:
        return

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    saved_bit_planes = []

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 5, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    for i in range(8):
        bit_plane = ((img >> i) & 1) * 255

        saved_bit_planes.append(bit_plane)

        plt.subplot(2, 5, i + 2)
        plt.imshow(bit_plane, cmap='gray')
        plt.title(f"Bit {i}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()


def save_images():

    if len(saved_bit_planes) == 0:
        return

    folder = filedialog.askdirectory(
        title="Select Folder to Save Images"
    )

    if not folder:
        return

    for i, plane in enumerate(saved_bit_planes):
        cv2.imwrite(f"{folder}/BitPlane_{i}.png", plane)

    print("Images Saved Successfully!")


root = tk.Tk()
root.title("Bit Plane Slicing")
root.geometry("450x560")

title = tk.Label(
    root,
    text="Bit Plane Slicing using Python",
    font=("Arial", 16, "bold")
)
title.pack(pady=15)

upload_btn = tk.Button(
    root,
    text="Upload Image",
    command=upload_image,
    width=20,
    height=2,
    bg="skyblue"
)
upload_btn.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

process_btn = tk.Button(
    root,
    text="Perform Bit Plane Slicing",
    command=bit_plane_slicing,
    width=25,
    height=2,
    bg="lightgreen"
)
process_btn.pack(pady=15)

save_btn = tk.Button(
    root,
    text="Save Images",
    command=save_images,
    width=25,
    height=2,
    bg="orange"
)
save_btn.pack(pady=10)

root.mainloop()