import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt

# Global Variables
image_path = None
global_img = None
adaptive_img = None


# Upload Image
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


# Histogram Equalization
def histogram_equalization():

    global global_img
    global adaptive_img

    if image_path is None:
        return

    # Read grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Global Histogram Equalization
    global_img = cv2.equalizeHist(img)

    # Adaptive Histogram Equalization (CLAHE)
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8,8)
    )

    adaptive_img = clahe.apply(img)

    # Normalized Histogram
    hist_original = cv2.calcHist([img],[0],None,[256],[0,256])
    hist_original = hist_original / hist_original.sum()

    hist_global = cv2.calcHist([global_img],[0],None,[256],[0,256])
    hist_global = hist_global / hist_global.sum()

    hist_adaptive = cv2.calcHist([adaptive_img],[0],None,[256],[0,256])
    hist_adaptive = hist_adaptive / hist_adaptive.sum()

    plt.figure(figsize=(14,10))

    # Original Image
    plt.subplot(3,2,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    # Original Histogram
    plt.subplot(3,2,2)
    plt.plot(hist_original,color="black")
    plt.title("Normalized Original Histogram")
    plt.xlim([0,256])

    # Global Equalization
    plt.subplot(3,2,3)
    plt.imshow(global_img,cmap='gray')
    plt.title("Global Histogram Equalization")
    plt.axis("off")

    # Global Histogram
    plt.subplot(3,2,4)
    plt.plot(hist_global,color="blue")
    plt.title("Normalized Global Histogram")
    plt.xlim([0,256])

    # Adaptive Equalization
    plt.subplot(3,2,5)
    plt.imshow(adaptive_img,cmap='gray')
    plt.title("Adaptive Histogram Equalization")
    plt.axis("off")

    # Adaptive Histogram
    plt.subplot(3,2,6)
    plt.plot(hist_adaptive,color="green")
    plt.title("Normalized Adaptive Histogram")
    plt.xlim([0,256])

    plt.tight_layout()
    plt.show()
    # Save Processed Images
def save_images():

    global global_img
    global adaptive_img

    if global_img is None or adaptive_img is None:
        return

    folder = filedialog.askdirectory(
        title="Select Folder to Save Images"
    )

    if not folder:
        return

    cv2.imwrite(folder + "/Global_Histogram_Equalization.png", global_img)
    cv2.imwrite(folder + "/Adaptive_Histogram_Equalization.png", adaptive_img)

    print("Images Saved Successfully!")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Histogram Equalization")
root.geometry("500x620")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Histogram Equalization using Python",
    font=("Arial",16,"bold")
)

title.pack(pady=15)

upload_btn = tk.Button(
    root,
    text="Upload Image",
    command=upload_image,
    width=25,
    height=2,
    bg="skyblue"
)

upload_btn.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

process_btn = tk.Button(
    root,
    text="Perform Histogram Equalization",
    command=histogram_equalization,
    width=30,
    height=2,
    bg="lightgreen"
)

process_btn.pack(pady=10)

save_btn = tk.Button(
    root,
    text="Save Processed Images",
    command=save_images,
    width=30,
    height=2,
    bg="orange"
)

save_btn.pack(pady=10)

exit_btn = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    width=30,
    height=2,
    bg="red",
    fg="white"
)

exit_btn.pack(pady=10)

root.mainloop()