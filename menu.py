import tkinter as tk
import subprocess
import sys
import os
from tkinter import ttk
from PIL import Image, ImageTk

def open_app(app_path):
    if app_path.endswith('.py'):
        subprocess.call([sys.executable, app_path])
    else:
        if sys.platform == "darwin":  # macOS
            subprocess.call(["open", app_path])
        elif sys.platform == "win32":  # Windows
            os.startfile(app_path)
        else:  # linux
            subprocess.call(["xdg-open", app_path])

root = tk.Tk()
root.title("Application Launcher")
root.configure(bg="Purple")

main_frame = tk.Frame(root, bg="purple")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

left_frame = tk.Frame(main_frame, bg="Purple")
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(main_frame, bg="Purple")
right_frame.pack(side="right", fill="both", expand=True, padx=20)

# Load and display an image at the top of the left frame
image_path = "/Users/chris-la4/Desktop/Final_project/IMG_4117.jpg"  # Update with your image path
image = Image.open(image_path)
image = image.resize((275, 200),)
image = ImageTk.PhotoImage(image)

image_label = tk.Label(left_frame, image=image, bg="Purple")
image_label.pack(pady=10)

# Add a text box at the top of the menu to introduce the menu
intro_label = tk.Label(left_frame, text="Christian's Apps", font=("Helvetica", 24, "bold"), bg="Purple", fg="white")
intro_label.pack(pady=10)

apps = {
    "WeatherApp_GUI": {
        "path": "/Users/chris-la4/Desktop/Final_project/WheatherApp_GUI/wheatherApp_GUI.py",
        "description": "A graphical user interface for checking weather conditions."
    },
    "Snake_Game": {
        "path": "/Users/chris-la4/Desktop/Final_project/Snake_Game/main.py",
        "description": "A classic snake game implemented in Python."
    },
    "Chaty": {
        "path": "/Users/chris-la4/Desktop/Final_project/Chaty/Chaty.py",
        "description": "A simple chat application."
    },
    "image_generator": {
        "path": "/Users/chris-la4/Desktop/Final_project/image_generator/main.py",
        "description": "An app that generates images based on input parameters."
    },
    "image_detector": {
        "path": "/Users/chris-la4/Desktop/Final_project/hgp_vision/vision.py",
        "description": "An image detection application."
    },
}

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10, background="white", foreground="black")

for app_name, app_info in apps.items():
    frame = tk.Frame(left_frame, bg="Purple")
    frame.pack(pady=10, padx=20, fill="x")

    button = ttk.Button(frame, text=app_name, command=lambda path=app_info["path"]: open_app(path), style="TButton")
    button.pack(side="left", fill="x", expand=True)

    text_box = tk.Entry(frame, width=50, font=("Helvetica", 12))
    text_box.insert(0, app_info["description"])
    text_box.pack(side="left", padx=10)

# Add an image box above the text box in the right frame
right_image_path = "/Users/chris-la4/Desktop/Final_project/IMG_3841.PNG"  # Update with your image path
right_image = Image.open(right_image_path)
right_image = right_image.resize((275, 200),)
right_image = ImageTk.PhotoImage(right_image)

right_image_label = tk.Label(right_frame, image=right_image, bg="Purple")
right_image_label.pack(pady=10)

# Add an additional text box to the right frame with a pre-filled message
message = (
    "Hi, I'm Christian! I am a creative and innovative person with a passion for developing "
    "applications that make a difference. My projects showcase my ability to bring ideas to life "
    "through code. I constantly strive to learn new technologies and improve my skills to create "
    "even more impactful solutions."
)
additional_text_box = tk.Text(right_frame, width=50, height=10, font=("Helvetica", 12))
additional_text_box.insert(tk.END, message)
additional_text_box.pack(pady=10)

root.mainloop()


