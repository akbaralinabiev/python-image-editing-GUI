# Let's import all the needed libraries
import tkinter as tk
from PIL import ImageTk, Image, ImageEnhance
from tkinter import filedialog

# First we create a global variable to store the current image
current_image = None

# Create a function to load an image from computer
def loadImage():
    global current_image

    image_path = filedialog.askopenfilename(
        filetypes=[('Image Files', '*.jpg;*.png;*.jpeg')])

    if not image_path:
        print("No image selected.")
        return

    try:
        current_image = Image.open(image_path)
    except IOError as e:
        tk.messagebox.showerror('Error', f'Failed to load image. Error: {e}')
        return



    # Save the image to the project folder
    current_image.save('original_image.jpg')

    # Load the saved image back into memory
    uploaded_image = Image.open('original_image.jpg')

#     # Display the modified image on the canvas
#     image_modified = ImageTk.PhotoImage(uploaded_image)
#     brighter_label.config(image=image_modified)


def addBrightness(image, brightness):
    uploaded_image = image.copy()
    uploaded_image = ImageEnhance.Brightness(
        uploaded_image).enhance(brightness)
    return uploaded_image


def addContrast(image, contrast):
    uploaded_image = image.copy()
    uploaded_image = ImageEnhance.Contrast(uploaded_image).enhance(contrast)
    return uploaded_image


def updateBrightness():
    global current_image, brighter_label

    new_brightness = brightness_slider.get()

    if not 0 <= new_brightness <= 2:
        tk.messagebox.showerror(
            'Error', 'Invalid brightness value. Please enter a value between 0 and 2.')
        return

    # Save the current image with the new brightness
    uploaded_image = addBrightness(current_image, new_brightness)
    uploaded_image.save(f"brightness_uploaded_image{new_brightness}.jpg")

    # Load the saved image back into memory
    uploaded_image = Image.open(f"brightness_uploaded_image{new_brightness}.jpg")

    # Apply brightness and display on brighter label
    brighter_label.config(image=ImageTk.PhotoImage(uploaded_image))


def updateContrast():
    global current_image, darker_label

    new_contrast = contrast_slider.get()

    if not 0 <= new_contrast <= 3:
        tk.messagebox.showerror(
            'Error', 'Invalid contrast value. Please enter a value between 0 and 3.')
        return

    # Save the current image with the new contrast
    uploaded_image = addContrast(current_image, new_contrast)
    uploaded_image.save(f"contrast_uploaded_image_{new_contrast}.jpg")

    # Load the saved image back into memory
    uploaded_image = Image.open(f"contrast_uploaded_image_{new_contrast}.jpg")

    # Apply contrast and display on darker label
    darker_label.config(image=ImageTk.PhotoImage(uploaded_image))



if __name__ == '__main__':
    window = tk.Tk()
    window.title('Image Editor')

    canvas = tk.Canvas(window, width=500, height=20)
    canvas.pack(fill='both', expand=True)

    brighter_label = tk.Label(canvas, image=None)
    darker_label = tk.Label(canvas, image=None)
    brighter_label.place(x=0, y=0, relwidth=0.5)

    darker_label.place(x=0.5, y=0, relwidth=0.5)

    load_button = tk.Button(window, text='Load Image', command=loadImage)
    load_button.pack(pady=10)

    load_button.pack(pady=10)

brightness_label = tk.Label(window, text='Brightness')
brightness_label.pack()

brightness_slider = tk.Scale(
    window, from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL)
brightness_slider.pack()

brightness_update_button = tk.Button(
    window, text='Apply Brightness', command=updateBrightness)
brightness_update_button.pack()

contrast_label = tk.Label(window, text='Contrast')
contrast_label.pack()

contrast_slider = tk.Scale(
    window, from_=0, to=3, resolution=0.01, orient=tk.HORIZONTAL)
contrast_slider.pack()

contrast_update_button = tk.Button(
    window, text='Apply Contrast', command=updateContrast)
contrast_update_button.pack()

brightness_slider.set(1)
contrast_slider.set(1)

window.mainloop()
