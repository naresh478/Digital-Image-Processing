import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt

# Global variable to store image path
image_path = None


# Function to upload image
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
        img.thumbnail((350, 350))

        photo = ImageTk.PhotoImage(img)

        image_label.config(image=photo)
        image_label.image = photo


# Function to perform Histogram Equalization
def histogram_equalization():

    if image_path is None:
        messagebox.showwarning("No Image", "Please upload an image first!")
        return

    # Read image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(img)

    # Display Results
    plt.figure(figsize=(12, 8))

    # Original Image
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Original Histogram
    plt.subplot(2, 2, 2)
    plt.hist(img.ravel(), bins=256, range=[0, 256], color='blue')
    plt.title("Original Histogram")

    # Equalized Image
    plt.subplot(2, 2, 3)
    plt.imshow(equalized, cmap='gray')
    plt.title("Equalized Image")
    plt.axis('off')

    # Equalized Histogram
    plt.subplot(2, 2, 4)
    plt.hist(equalized.ravel(), bins=256, range=[0, 256], color='green')
    plt.title("Equalized Histogram")

    plt.tight_layout()
    plt.show()


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Histogram Equalization")
root.geometry("500x600")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Histogram Equalization",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

upload_btn = tk.Button(
    root,
    text="Upload Image",
    command=upload_image,
    width=20,
    height=2,
    bg="skyblue",
    font=("Arial", 11)
)
upload_btn.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=15)

equalize_btn = tk.Button(
    root,
    text="Perform Histogram Equalization",
    command=histogram_equalization,
    width=30,
    height=2,
    bg="lightgreen",
    font=("Arial", 11)
)
equalize_btn.pack(pady=20)

root.mainloop()